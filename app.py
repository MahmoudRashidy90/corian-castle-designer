#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
كوريان كاسيل - تطبيق Flask الرئيسي
=====================================
تطبيق تصميم تفاعلي بالذكاء الاصطناعي
"""

import os
import json
import time
import logging
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
import requests
from PIL import Image
import io
import base64
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

# إنشاء تطبيق Flask
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'corian-castle-secret-2025')

# ========================================
# إعدادات التطبيق
# ========================================

# مجلدات التخزين
UPLOAD_FOLDER = 'uploads'
GENERATED_FOLDER = 'static/generated_designs'
TEMPLATES_FOLDER = 'templates'
LOGS_FOLDER = 'logs'

# أنواع الملفات المسموحة
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'dwg', 'ai', 'psd'}

# حد أقصى لحجم الملف (16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# إنشاء المجلدات إذا لم تكن موجودة
for folder in [UPLOAD_FOLDER, GENERATED_FOLDER, LOGS_FOLDER]:
    os.makedirs(folder, exist_ok=True)

# ========================================
# إعداد نظام الـ Logging
# ========================================

def setup_logging():
    """إعداد نظام تسجيل الأحداث"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'{LOGS_FOLDER}/app.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

setup_logging()
logger = logging.getLogger(__name__)

def log_activity(message):
    """تسجيل نشاط المستخدمين"""
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(f'{LOGS_FOLDER}/activity.log', 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")
        logger.info(message)
    except Exception as e:
        logger.error(f"خطأ في تسجيل النشاط: {e}")

# ========================================
# دوال مساعدة
# ========================================

def allowed_file(filename):
    """فحص نوع الملف المسموح"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_huggingface_token():
    """الحصول على توكن Hugging Face"""
    return os.getenv('HUGGINGFACE_API_TOKEN')

def test_huggingface_connection():
    """اختبار الاتصال مع Hugging Face API"""
    token = get_huggingface_token()
    if not token:
        return False, "لم يتم العثور على HUGGINGFACE_API_TOKEN"
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get("https://huggingface.co/api/whoami", headers=headers, timeout=10)
        if response.status_code == 200:
            user_info = response.json()
            return True, f"متصل بـ Hugging Face - المستخدم: {user_info.get('name', 'Unknown')}"
        else:
            return False, f"خطأ في التوكن - كود الاستجابة: {response.status_code}"
    except Exception as e:
        return False, f"خطأ في الاتصال: {str(e)}"

# ========================================
# الصفحات الرئيسية (Routes)
# ========================================

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    log_activity("زيارة الصفحة الرئيسية")
    return render_template('index.html')

@app.route('/designer')
def designer():
    """صفحة المصمم التفاعلي"""
    log_activity("دخول صفحة المصمم التفاعلي")
    return render_template('designer.html')

@app.route('/upload-design')
def upload_design():
    """صفحة رفع التصاميم الجاهزة"""
    log_activity("دخول صفحة رفع التصاميم")
    return render_template('upload-design.html')

@app.route('/confirm-design')
def confirm_design():
    """صفحة تأكيد التصميم"""
    design_id = request.args.get('id', 'DS-2025-001')
    status = request.args.get('status', 'completed')
    log_activity(f"عرض تأكيد التصميم: {design_id}")
    return render_template('confirm_design.html')

@app.route('/admin')
def admin():
    """لوحة تحكم الإدارة"""
    log_activity("دخول لوحة الإدارة")
    return render_template('admin.html')

# ========================================
# APIs للذكاء الاصطناعي
# ========================================

@app.route('/api/test-ai-token')
def test_ai_token():
    """اختبار صحة توكن Hugging Face"""
    log_activity("🔍 اختبار توكن الذكاء الاصطناعي")
    
    success, message = test_huggingface_connection()
    
    result = {
        'status': 'success' if success else 'error',
        'message': message,
        'valid': success,
        'timestamp': datetime.now().isoformat()
    }
    
    if success:
        log_activity(f"✅ نجح اختبار التوكن: {message}")
    else:
        log_activity(f"❌ فشل اختبار التوكن: {message}")
    
    return jsonify(result)

@app.route('/api/generate-ai', methods=['POST'])
def generate_ai():
    """توليد صورة بالذكاء الاصطناعي"""
    try:
        log_activity("🚀 بدء طلب توليد AI")
        
        # استلام البيانات
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'لم يتم إرسال بيانات'}), 400
        
        prompt = data.get('prompt', '').strip()
        width = data.get('width', 768)
        height = data.get('height', 768)
        
        if not prompt:
            return jsonify({'success': False, 'error': 'يرجى إدخال وصف للتصميم'}), 400
        
        if len(prompt) < 10:
            return jsonify({'success': False, 'error': 'الوصف قصير جداً، اكتب تفاصيل أكثر'}), 400
        
        # الحصول على التوكن
        token = get_huggingface_token()
        if not token:
            log_activity("❌ خطأ: HUGGINGFACE_API_TOKEN غير موجود")
            return jsonify({'success': False, 'error': 'خدمة الذكاء الاصطناعي غير متاحة'}), 500
        
        log_activity(f"📝 بدء توليد AI للوصف: {prompt[:50]}...")
        
        # تحسين النص للتصاميم المعمارية
        enhanced_prompt = f"professional interior design, {prompt}, modern architecture, high quality rendering, photorealistic, 8K, corian countertops"
        
        # استدعاء Hugging Face API
        result = call_huggingface_api(enhanced_prompt, token, width, height)
        
        if result['success']:
            log_activity(f"✅ نجح التوليد: {result['filename']}")
            return jsonify({
                'success': True,
                'image_url': result['image_url'],
                'filename': result['filename'],
                'prompt_used': enhanced_prompt,
                'generation_time': result.get('time', 0),
                'model': result.get('model_used', 'Stable Diffusion')
            })
        else:
            log_activity(f"❌ فشل التوليد: {result['error']}")
            return jsonify({'success': False, 'error': result['error']}), 503
    
    except Exception as e:
        log_activity(f"❌ خطأ في generate_ai: {str(e)}")
        return jsonify({'success': False, 'error': 'حدث خطأ غير متوقع'}), 500

def call_huggingface_api(prompt, token, width=768, height=768):
    """استدعاء Hugging Face API"""
    models = [
        "runwayml/stable-diffusion-v1-5",
        "stabilityai/stable-diffusion-2-1"
    ]
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "num_inference_steps": 30,
            "guidance_scale": 7.5,
            "width": width,
            "height": height
        }
    }
    
    start_time = time.time()
    
    # جرب كل model
    for i, model in enumerate(models):
        try:
            api_url = f"https://api-inference.huggingface.co/models/{model}"
            log_activity(f"🤖 جاري التجربة مع Model {i+1}: {model}")
            
            response = requests.post(api_url, headers=headers, json=payload, timeout=120)
            
            if response.status_code == 200:
                # حفظ الصورة
                timestamp = int(time.time())
                filename = f"ai_design_{timestamp}.jpg"
                filepath = os.path.join(GENERATED_FOLDER, filename)
                
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                
                generation_time = round(time.time() - start_time, 2)
                log_activity(f"✅ تم حفظ الصورة: {filepath}")
                
                return {
                    'success': True,
                    'image_url': f"/static/generated_designs/{filename}",
                    'filename': filename,
                    'filepath': filepath,
                    'model_used': model,
                    'time': generation_time
                }
            
            elif response.status_code == 503:
                log_activity(f"⏳ Model {i+1} مشغول، جاري المحاولة مع التالي...")
                if i == 0:  # انتظار فقط للـ model الأول
                    time.sleep(20)
                continue
            
            else:
                log_activity(f"❌ خطأ في Model {i+1}: {response.status_code}")
                continue
        
        except Exception as e:
            log_activity(f"❌ خطأ مع Model {i+1}: {str(e)}")
            continue
    
    # إذا فشلت كل المحاولات
    return {
        'success': False,
        'error': 'جميع خدمات الذكاء الاصطناعي مشغولة حالياً، يرجى المحاولة بعد قليل'
    }

# ========================================
# APIs للملفات والرفع
# ========================================

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """رفع ملف"""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'لم يتم اختيار ملف'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'لم يتم اختيار ملف'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = int(time.time())
            filename = f"{timestamp}_{filename}"
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            
            log_activity(f"تم رفع ملف: {filename}")
            
            return jsonify({
                'success': True,
                'filename': filename,
                'file_path': file_path,
                'message': 'تم رفع الملف بنجاح'
            })
        
        return jsonify({'success': False, 'error': 'نوع الملف غير مدعوم'}), 400
    
    except Exception as e:
        log_activity(f"خطأ في رفع الملف: {str(e)}")
        return jsonify({'success': False, 'error': 'حدث خطأ في رفع الملف'}), 500

@app.route('/api/save-drawing', methods=['POST'])
def save_drawing():
    """حفظ الرسم من Canvas"""
    try:
        data = request.get_json()
        canvas_data = data.get('canvas_data')
        
        if canvas_data:
            # إزالة البادئة من Base64
            image_data = canvas_data.split(',')[1]
            
            # تحويل إلى صورة
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
            
            # حفظ الصورة
            timestamp = int(time.time())
            filename = f"drawing_{timestamp}.png"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            image.save(filepath)
            
            log_activity(f"تم حفظ الرسم: {filename}")
            
            return jsonify({
                'success': True,
                'filename': filename,
                'filepath': filepath,
                'message': 'تم حفظ الرسم بنجاح'
            })
    
    except Exception as e:
        log_activity(f"خطأ في حفظ الرسم: {str(e)}")
        return jsonify({'success': False, 'error': 'حدث خطأ في حفظ الرسم'}), 500

# ========================================
# APIs للإحصائيات والإدارة
# ========================================

@app.route('/api/stats')
def get_stats():
    """جلب إحصائيات النظام"""
    try:
        # إحصائيات بسيطة
        uploads_count = 0
        generated_count = 0
        
        if os.path.exists(UPLOAD_FOLDER):
            uploads_count = len([f for f in os.listdir(UPLOAD_FOLDER) 
                               if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        
        if os.path.exists(GENERATED_FOLDER):
            generated_count = len([f for f in os.listdir(GENERATED_FOLDER) 
                                 if f.lower().endswith('.jpg')])
        
        # فحص حالة التوكن
        token_status = 'configured' if get_huggingface_token() else 'missing'
        
        stats = {
            'total_uploads': uploads_count,
            'total_generated': generated_count,
            'server_status': 'active',
            'token_status': token_status,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(stats)
    
    except Exception as e:
        log_activity(f"خطأ في جلب الإحصائيات: {str(e)}")
        return jsonify({'error': f'خطأ في جلب الإحصائيات: {str(e)}'}), 500

# ========================================
# Static Files Routes
# ========================================

@app.route('/static/generated_designs/<filename>')
def generated_file(filename):
    """عرض الملفات المولدة"""
    return send_from_directory(GENERATED_FOLDER, filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """عرض الملفات المرفوعة"""
    return send_from_directory(UPLOAD_FOLDER, filename)

# ========================================
# معالجة الأخطاء
# ========================================

@app.errorhandler(404)
def page_not_found(e):
    """صفحة غير موجودة"""
    log_activity(f"صفحة غير موجودة: {request.url}")
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """خطأ في الخادم"""
    log_activity(f"خطأ في الخادم: {str(e)}")
    return jsonify({'error': 'خطأ في الخادم - يرجى المحاولة لاحقاً'}), 500

@app.errorhandler(413)
def too_large(e):
    """حجم الملف كبير"""
    return jsonify({'error': 'حجم الملف كبير جداً (الحد الأقصى 16MB)'}), 413

# ========================================
# تشغيل التطبيق
# ========================================
# ========================================
# APIs مفقودة - أضف هذا قبل if __name__ == '__main__':
# ========================================

@app.route('/submit-design', methods=['POST'])
def submit_design():
    """معالجة التصميم من صفحة المصمم"""
    try:
        log_activity("📝 استلام تصميم جديد")
        
        # استلام البيانات
        customer_name = request.form.get('customerName', '').strip()
        whatsapp = request.form.get('whatsapp', '').strip()
        project_type = request.form.get('projectType', '')
        
        # التحقق من البيانات
        if not customer_name or not whatsapp or not project_type:
            flash('يرجى ملء جميع الحقول المطلوبة', 'error')
            return redirect(url_for('designer'))
        
        # إنشاء ID للتصميم
        design_id = f"DS-{datetime.now().strftime('%Y')}-{str(int(time.time()))[-3:]}"
        
        # بيانات التصميم
        design_data = {
            'design_id': design_id,
            'customer_name': customer_name,
            'whatsapp': whatsapp,
            'project_type': project_type,
            'status': 'completed',
            'timestamp': datetime.now().isoformat()
        }
        
        # حفظ في مجلد designs
        os.makedirs('designs', exist_ok=True)
        with open(f"designs/{design_id}.json", 'w', encoding='utf-8') as f:
            json.dump(design_data, f, ensure_ascii=False, indent=2)
        
        log_activity(f"✅ تم حفظ التصميم: {design_id}")
        
        # توجيه لصفحة التأكيد
        return redirect(url_for('confirm_design', id=design_id, status='completed'))
    
    except Exception as e:
        log_activity(f"❌ خطأ في التصميم: {str(e)}")
        flash('حدث خطأ، يرجى المحاولة مرة أخرى', 'error')
        return redirect(url_for('designer'))

@app.route('/upload-design', methods=['POST'])
def upload_design_form():
    """معالجة رفع التصاميم"""
    try:
        log_activity("📤 استلام تصميم مرفوع")
        
        # استلام البيانات
        customer_name = request.form.get('customerName', '').strip()
        whatsapp = request.form.get('whatsapp', '').strip()
        service_type = request.form.get('serviceType', '')
        
        # التحقق من البيانات
        if not customer_name or not whatsapp or not service_type:
            return jsonify({
                'success': False, 
                'error': 'يرجى ملء جميع الحقول المطلوبة'
            }), 400
        
        # معالجة الملفات
        uploaded_files = []
        if 'designFiles' in request.files:
            files = request.files.getlist('designFiles')
            for file in files:
                if file and file.filename and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    timestamp = int(time.time())
                    filename = f"upload_{timestamp}_{filename}"
                    file_path = os.path.join(UPLOAD_FOLDER, filename)
                    file.save(file_path)
                    uploaded_files.append(filename)
        
        # إنشاء ID
        design_id = f"UD-{datetime.now().strftime('%Y')}-{str(int(time.time()))[-3:]}"
        
        # بيانات التصميم
        design_data = {
            'design_id': design_id,
            'customer_name': customer_name,
            'whatsapp': whatsapp,
            'service_type': service_type,
            'uploaded_files': uploaded_files,
            'status': 'pending',
            'timestamp': datetime.now().isoformat()
        }
        
        # حفظ البيانات
        os.makedirs('designs', exist_ok=True)
        with open(f"designs/{design_id}.json", 'w', encoding='utf-8') as f:
            json.dump(design_data, f, ensure_ascii=False, indent=2)
        
        log_activity(f"✅ تم حفظ التصميم المرفوع: {design_id}")
        
        return jsonify({
            'success': True,
            'design_id': design_id,
            'message': 'تم رفع التصميم بنجاح'
        })
    
    except Exception as e:
        log_activity(f"❌ خطأ في الرفع: {str(e)}")
        return jsonify({
            'success': False, 
            'error': 'حدث خطأ في الرفع'
        }), 500

@app.route('/api/designs')
def get_designs():
    """جلب جميع التصاميم للإدارة"""
    try:
        designs = []
        designs_folder = 'designs'
        
        if os.path.exists(designs_folder):
            for filename in os.listdir(designs_folder):
                if filename.endswith('.json'):
                    with open(f"{designs_folder}/{filename}", 'r', encoding='utf-8') as f:
                        design = json.load(f)
                        designs.append(design)
        
        # ترتيب حسب التاريخ
        designs.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        
        return jsonify(designs)
    
    except Exception as e:
        return jsonify({'error': 'خطأ في جلب البيانات'}), 500

@app.route('/api/design/<design_id>')
def get_design(design_id):
    """جلب تصميم محدد"""
    try:
        design_file = f"designs/{design_id}.json"
        
        if os.path.exists(design_file):
            with open(design_file, 'r', encoding='utf-8') as f:
                design = json.load(f)
            return jsonify(design)
        else:
            return jsonify({'error': 'التصميم غير موجود'}), 404
    
    except Exception as e:
        return jsonify({'error': 'خطأ في جلب التصميم'}), 500
if __name__ == '__main__':
    log_activity("🚀 بدء تشغيل خادم كوريان كاسيل")
    
    # فحص حالة النظام عند البداية
    token_check, token_message = test_huggingface_connection()
    
    print("=" * 60)
    print("🏠 كوريان كاسيل - خادم التطبيق")
    print("=" * 60)
    print(f"🌐 الرابط: http://localhost:5000")
    print(f"🔧 اختبار التوكن: http://localhost:5000/api/test-ai-token")
    print(f"🎨 صفحة التصميم: http://localhost:5000/designer")
    print(f"📤 رفع التصاميم: http://localhost:5000/upload-design")
    print(f"⚙️ لوحة الإدارة: http://localhost:5000/admin")
    print("=" * 60)
    print(f"🤖 حالة AI Token: {'✅ يعمل' if token_check else '❌ يحتاج فحص'}")
    if not token_check:
        print(f"   السبب: {token_message}")
    print("=" * 60)
    
    # تشغيل التطبيق
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=True
    )

# ========================================
# متغير للـ WSGI Server
# ========================================

# هذا المتغير مطلوب لـ passenger_wsgi.py
application = app