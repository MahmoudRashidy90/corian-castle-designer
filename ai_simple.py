# ai_simple.py - ذكاء اصطناعي مبسط للبداية
import os
import requests
import time
from PIL import Image
import io

class SimpleAI:
    def __init__(self):
        self.token = os.getenv('HUGGINGFACE_API_TOKEN')
        self.api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    def generate(self, prompt):
        """توليد صورة من النص"""
        
        try:
            print(f"🤖 بدء التوليد...")
            print(f"📝 النص: {prompt[:100]}...")
            
            # إرسال الطلب
            response = requests.post(
                self.api_url, 
                headers=self.headers, 
                json={"inputs": prompt},
                timeout=60
            )
            
            print(f"📡 رد الخادم: {response.status_code}")
            
            if response.status_code == 200:
                # حفظ الصورة
                image = Image.open(io.BytesIO(response.content))
                filename = f"ai_generated_{int(time.time())}.png"
                filepath = f"generated_designs/{filename}"
                
                # إنشاء المجلد إذا لم يكن موجود
                os.makedirs('generated_designs', exist_ok=True)
                image.save(filepath)
                
                print(f"✅ تم الحفظ: {filepath}")
                
                return {
                    'success': True,
                    'path': filepath,
                    'url': f"http://localhost:5000/generated_designs/{filename}"
                }
            
            elif response.status_code == 503:
                print("⏳ النموذج يُحمَّل... انتظر 20 ثانية")
                time.sleep(20)
                return self.generate(prompt)  # محاولة أخرى
            
            else:
                print(f"❌ خطأ API: {response.status_code}")
                print(f"📄 التفاصيل: {response.text}")
                return {'success': False, 'error': response.text}
                
        except Exception as e:
            print(f"❌ خطأ عام: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    def create_prompt(self, design_data):
        """تحويل بيانات التصميم لنص إنجليزي"""
        
        project_type = design_data.get('projectType', 'مطبخ')
        material = design_data.get('material', 'corian')
        
        # ترجمة النوع
        types = {
            'مطبخ': 'modern kitchen',
            'مغسلة': 'bathroom vanity', 
            'كاونتر': 'reception counter',
            'دولاب تلفزيون': 'TV cabinet',
            'دريسنق رووم': 'walk-in closet'
        }
        
        eng_type = types.get(project_type, 'kitchen')
        
        # بناء النص
        prompt = f"""
        Professional {eng_type} design with {material} countertops,
        modern contemporary style, clean minimalist lines,
        photorealistic interior design render,
        high quality architectural visualization,
        professional lighting, 4K detailed
        """
        
        return prompt.strip()

# اختبار بسيط
def test_ai():
    """اختبار الذكاء الاصطناعي"""
    
    print("🧪 اختبار الذكاء الاصطناعي...")
    print("=" * 50)
    
    # التحقق من التوكن
    token = os.getenv('HUGGINGFACE_API_TOKEN')
    if not token:
        print("❌ لم يتم العثور على HUGGINGFACE_API_TOKEN")
        print("💡 أضف التوكن في ملف .env")
        return False
    
    if not token.startswith('hf_'):
        print("❌ التوكن غير صحيح (يجب أن يبدأ بـ hf_)")
        return False
    
    print(f"✅ التوكن موجود: {token[:10]}...")
    
    # إنشاء الذكاء الاصطناعي
    ai = SimpleAI()
    
    # بيانات تجريبية
    test_data = {
        'projectType': 'مطبخ',
        'material': 'LG'
    }
    
    # إنشاء النص
    prompt = ai.create_prompt(test_data)
    print(f"📝 النص المولد: {prompt}")
    
    # توليد الصورة
    result = ai.generate(prompt)
    
    if result['success']:
        print("🎉 نجح التوليد!")
        print(f"📁 مسار الملف: {result['path']}")
        print(f"🌐 الرابط: {result['url']}")
        
        # التحقق من وجود الملف
        if os.path.exists(result['path']):
            print("✅ الملف محفوظ بنجاح")
            
            # حجم الملف
            size = os.path.getsize(result['path'])
            print(f"📊 حجم الملف: {size / 1024:.1f} KB")
            
        return True
    else:
        print("❌ فشل التوليد")
        print(f"🔍 السبب: {result.get('error', 'غير معروف')}")
        return False

if __name__ == "__main__":
    # تحميل متغيرات البيئة
    from dotenv import load_dotenv
    load_dotenv()
    
    # تشغيل الاختبار
    success = test_ai()
    
    if success:
        print("\n🎊 الذكاء الاصطناعي يعمل!")
        print("🚀 جاهز للخطوة التالية")
    else:
        print("\n❌ يحتاج إصلاح")
        print("💡 تحقق من:")
        print("  - وجود ملف .env")
        print("  - صحة HUGGINGFACE_API_TOKEN") 
        print("  - اتصال الإنترنت")