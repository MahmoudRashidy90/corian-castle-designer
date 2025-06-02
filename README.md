# صممها بنفسك - كوريان كاسيل 🏠✨

> **منصة تصميم تفاعلية بالذكاء الاصطناعي لتحويل الرسوم اليدوية إلى تصاميم واقعية للمطابخ والمغاسل**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-green.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/flask-2.3+-red.svg)](https://flask.palletsprojects.com)
[![Status](https://img.shields.io/badge/status-production--ready-brightgreen.svg)]()

---

## 📋 **فهرس المحتويات**

- [🎯 نظرة عامة](#-نظرة-عامة)
- [✨ المميزات](#-المميزات)
- [🏗️ هيكل المشروع](#️-هيكل-المشروع)
- [⚙️ التثبيت والإعداد](#️-التثبيت-والإعداد)
- [🔧 إعداد المتغيرات](#-إعداد-المتغيرات)
- [🚀 تشغيل المشروع](#-تشغيل-المشروع)
- [📱 استخدام النظام](#-استخدام-النظام)
- [🐳 النشر بـ Docker](#-النشر-بـ-docker)
- [🔌 APIs المتاحة](#-apis-المتاحة)
- [🛠️ استكشاف الأخطاء](#️-استكشاف-الأخطاء)
- [📊 مراقبة الأداء](#-مراقبة-الأداء)
- [🤝 المساهمة](#-المساهمة)
- [📞 الدعم التقني](#-الدعم-التقني)

---

## 🎯 **نظرة عامة**

**كوريان كاسيل** هي منصة تفاعلية مبتكرة تمكن العملاء من تصميم مطابخهم ومغاسلهم بأنفسهم أو رفع تصاميم جاهزة، مع استخدام الذكاء الاصطناعي لتحويل الرسوم البسيطة إلى تصاميم واقعية ثلاثية الأبعاد.

### **🎨 الفكرة الأساسية**
- العميل يرسم تصميمه بشكل بسيط على الموقع
- الذكاء الاصطناعي يحول الرسمة لتصميم واقعي
- إرسال النتيجة تلقائياً على واتساب
- فريق كوريان كاسيل يتواصل لبدء التنفيذ

---

## ✨ **المميزات**

### **🎨 للعملاء**
- **رسم تفاعلي مباشر** على المتصفح بالماوس أو اللمس
- **رفع تصاميم جاهزة** مع أنواع ملفات متعددة
- **5 أنواع مشاريع مدعومة**: مطبخ، مغسلة، كاونتر، دولاب تلفزيون، دريسنق رووم
- **حقول متخصصة** لكل نوع مشروع مع تفاصيل دقيقة
- **إرسال تلقائي على واتساب** مع تفاصيل كاملة
- **واجهة باللغة العربية** مع محتوى كويتي محلي

### **🤖 التقنيات المتقدمة**
- **ذكاء اصطناعي متطور** (Replicate API) لتحويل الرسوم
- **معالجة صور متقدمة** مع ضغط تلقائي
- **تكامل واتساب** عبر Twilio أو WhatsApp Business API
- **تصميم متجاوب** يعمل على جميع الأجهزة
- **حفظ تلقائي** للبيانات أثناء التصميم

### **📊 للإدارة**
- **لوحة تحكم شاملة** لمتابعة الطلبات
- **إحصائيات مباشرة** مع فلاتر متقدمة
- **إدارة حالات الطلبات** مع إشعارات
- **تصدير البيانات** بصيغة CSV للتقارير
- **واجهة سهلة الاستخدام** مع بحث سريع

---

## 🏗️ **هيكل المشروع**

```
corian-castle/
│
├── 📁 Backend
│   ├── app.py                 # خادم Flask الرئيسي
│   ├── requirements.txt       # المكتبات المطلوبة
│   └── .env                   # متغيرات البيئة
│
├── 📁 Frontend Templates
│   ├── index.html            # الصفحة الرئيسية
│   ├── designer.html         # صفحة التصميم التفاعلي
│   ├── upload-design.html    # رفع التصاميم الجاهزة
│   ├── confirm_design.html   # تأكيد وعرض النتائج
│   └── admin.html           # لوحة تحكم الإدارة
│
├── 📁 Storage
│   ├── uploads/             # الملفات المرفوعة
│   ├── designs/            # بيانات التصاميم (JSON)
│   ├── generated_designs/  # التصاميم المولدة بالـ AI
│   └── logs/              # ملفات السجلات
│
├── 📁 Docker
│   ├── Dockerfile          # إعدادات Docker
│   ├── docker-compose.yml  # خدمات Docker Compose
│   └── nginx.conf          # إعدادات Nginx
│
└── 📖 Documentation
    ├── README.md           # هذا الملف
    └── API_DOCS.md        # توثيق APIs
```

---

## ⚙️ **التثبيت والإعداد**

### **📋 المتطلبات الأساسية**

```bash
# Python 3.9 أو أحدث
python --version

# pip (مدير حزم Python)
pip --version

# Git (لاستنساخ المشروع)
git --version
```

### **1️⃣ استنساخ المشروع**

```bash
# استنساخ المستودع
git clone https://github.com/your-username/corian-castle.git
cd corian-castle

# أو تحميل مباشر
wget https://github.com/your-username/corian-castle/archive/main.zip
unzip main.zip && cd corian-castle-main
```

### **2️⃣ إنشاء البيئة الافتراضية**

```bash
# إنشاء البيئة الافتراضية
python -m venv venv

# تفعيل البيئة
# على Linux/Mac:
source venv/bin/activate

# على Windows:
venv\Scripts\activate

# التأكد من التفعيل
which python  # يجب أن يظهر مسار venv
```

### **3️⃣ تثبيت المكتبات**

```bash
# تحديث pip
pip install --upgrade pip

# تثبيت المتطلبات
pip install -r requirements.txt

# للتطوير (اختياري)
pip install -r requirements-dev.txt
```

### **4️⃣ إنشاء المجلدات المطلوبة**

```bash
# إنشاء مجلدات التخزين
mkdir -p uploads designs generated_designs logs

# تعيين الأذونات (Linux/Mac)
chmod 755 uploads designs generated_designs logs

# على Windows
# استخدم File Explorer أو PowerShell
```

---

## 🔧 **إعداد المتغيرات**

### **📝 إنشاء ملف .env**

```bash
# نسخ النموذج
cp .env.example .env

# تحرير الملف
nano .env  # أو أي محرر نصوص
```

### **🔑 المتغيرات المطلوبة**

```env
# ═══════════════════════════════════════════════════════
# Flask Configuration
# ═══════════════════════════════════════════════════════
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-super-secret-key-here-change-this-in-production

# ═══════════════════════════════════════════════════════
# Replicate AI Configuration
# ═══════════════════════════════════════════════════════
REPLICATE_API_TOKEN=r8_your-replicate-api-token-here

# ═══════════════════════════════════════════════════════
# WhatsApp API Configuration
# ═══════════════════════════════════════════════════════

# خيار 1: Twilio (الأسهل)
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=+14155238886

# خيار 2: WhatsApp Business API
WHATSAPP_API_URL=https://graph.facebook.com/v17.0/YOUR_PHONE_NUMBER_ID/messages
WHATSAPP_TOKEN=your-whatsapp-business-api-token

# ═══════════════════════════════════════════════════════
# Upload Configuration
# ═══════════════════════════════════════════════════════
MAX_CONTENT_LENGTH=10485760  # 10MB
UPLOAD_FOLDER=uploads
ALLOWED_EXTENSIONS=png,jpg,jpeg,gif,pdf,dwg,ai,psd

# ═══════════════════════════════════════════════════════
# Domain Configuration
# ═══════════════════════════════════════════════════════
DOMAIN_URL=https://yoursite.com
LOCAL_URL=http://localhost:5000

# ═══════════════════════════════════════════════════════
# Database (للمستقبل)
# ═══════════════════════════════════════════════════════
# DATABASE_URL=postgresql://user:password@localhost/corian_db

# ═══════════════════════════════════════════════════════
# Redis (للإنتاج)
# ═══════════════════════════════════════════════════════
# REDIS_URL=redis://localhost:6379/0
```

### **🔐 الحصول على API Keys**

#### **Replicate API**
1. سجل في [Replicate.com](https://replicate.com)
2. اذهب إلى [Account Settings](https://replicate.com/account)
3. انسخ الـ API Token وضعه في `.env`

#### **Twilio WhatsApp** (الأسهل)
1. سجل في [Twilio](https://twilio.com)
2. من Console، احصل على:
   - Account SID
   - Auth Token
   - WhatsApp Phone Number
3. اتبع [Twilio WhatsApp Setup Guide](https://www.twilio.com/docs/whatsapp)

#### **WhatsApp Business API** (للشركات)
1. سجل في [Facebook Developers](https://developers.facebook.com)
2. أنشئ تطبيق Business
3. احصل على Phone Number ID و Access Token
4. اتبع [WhatsApp Business Setup](https://developers.facebook.com/docs/whatsapp)

---

## 🚀 **تشغيل المشروع**

### **🔧 للتطوير**

```bash
# تفعيل البيئة الافتراضية
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate     # Windows

# تشغيل الخادم
python app.py

# أو باستخدام Flask
flask run --host=0.0.0.0 --port=5000

# الوصول للموقع
# http://localhost:5000
```

### **📊 مراقبة السجلات**

```bash
# مراقبة سجلات Flask
tail -f logs/app.log

# مراقبة جميع السجلات
tail -f logs/*.log

# فحص أخطاء محددة
grep "ERROR" logs/app.log
```

### **⚡ إعادة التشغيل السريع**

```bash
# إيقاف الخادم: Ctrl+C

# إعادة تشغيل
python app.py

# أو للتطوير مع Auto-reload
FLASK_ENV=development flask run --reload
```

---

## 📱 **استخدام النظام**

### **👥 للعملاء**

#### **🎨 التصميم التفاعلي**
1. **اختر نوع المشروع** (مطبخ، مغسلة، إلخ)
2. **املأ بياناتك الشخصية** والموقع
3. **اختر طريقة التصميم**:
   - ارسم بنفسك على الكانفاس
   - ارفع صورة من جهازك
4. **املأ التفاصيل المتخصصة** للمشروع
5. **اضغط "أنشئ التصميم"**
6. **انتظر النتيجة على واتساب**

#### **📤 رفع تصميم جاهز**
1. **اختر نوع الخدمة** (تنفيذ حرفي، تطوير، استشارة)
2. **املأ بياناتك**
3. **ارفع الملفات** (صور، PDF، DWG، إلخ)
4. **اكتب وصف مفصل** للمتطلبات
5. **اضغط "أرسل طلبي"**
6. **انتظر الرد خلال 24 ساعة**

### **👨‍💼 للإدارة**

#### **📊 لوحة التحكم** (`/admin`)
- **مراقبة الإحصائيات** المباشرة
- **فلترة الطلبات** حسب الحالة والنوع
- **البحث السريع** بالاسم أو رقم الطلب
- **عرض تفاصيل كاملة** لكل طلب
- **تحديث حالات الطلبات**
- **إرسال رسائل واتساب** مباشرة
- **تصدير التقارير** بصيغة CSV

#### **🔄 إدارة الطلبات**
```
الحالات المتاحة:
├── pending      → في الانتظار
├── processing   → قيد المعالجة  
├── completed    → مكتملة
└── failed       → فاشلة
```

---

## 🐳 **النشر بـ Docker**

### **🔨 البناء والتشغيل**

```bash
# بناء الصورة
docker build -t corian-castle .

# تشغيل الحاوية
docker run -d \
  --name corian-castle \
  -p 5000:5000 \
  --env-file .env \
  -v $(pwd)/uploads:/app/uploads \
  -v $(pwd)/designs:/app/designs \
  corian-castle

# فحص الحالة
docker ps
docker logs corian-castle
```

### **🐙 باستخدام Docker Compose**

```bash
# تشغيل جميع الخدمات
docker-compose up -d

# مراقبة السجلات
docker-compose logs -f

# إيقاف الخدمات
docker-compose down

# إعادة البناء والتشغيل
docker-compose up --build -d
```

### **📋 خدمات Docker Compose**

```yaml
الخدمات المتاحة:
├── app      → التطبيق الرئيسي (Flask)
├── redis    → التخزين المؤقت (للجلسات)
└── nginx    → خادم الويب (Reverse Proxy)
```

### **🔧 إعدادات الإنتاج**

```bash
# تحديث المتغيرات للإنتاج
sed -i 's/FLASK_ENV=development/FLASK_ENV=production/' .env
sed -i 's/FLASK_DEBUG=True/FLASK_DEBUG=False/' .env

# إعادة التشغيل
docker-compose restart app
```

---

## 🔌 **APIs المتاحة**

### **📋 نظرة عامة**

| HTTP Method | Endpoint | الوصف |
|-------------|----------|--------|
| `GET` | `/` | الصفحة الرئيسية |
| `GET` | `/designer.html` | صفحة التصميم |
| `GET` | `/upload-design.html` | صفحة رفع التصاميم |
| `GET` | `/admin` | لوحة التحكم |
| `POST` | `/submit-design` | إرسال تصميم جديد |
| `POST` | `/upload-design` | رفع تصميم جاهز |
| `GET` | `/api/designs` | جلب جميع التصاميم |
| `GET` | `/api/design/{id}` | جلب تفاصيل تصميم |

### **📤 POST /submit-design**

إرسال تصميم جديد من صفحة التصميم التفاعلي.

**Request:**
```bash
curl -X POST http://localhost:5000/submit-design \
  -F "customerName=أحمد محمد" \
  -F "whatsapp=96599123456" \
  -F "location=حولي" \
  -F "projectType=مطبخ" \
  -F "width=3.5" \
  -F "height=2.8" \
  -F "material=LG" \
  -F "projectSketch=@drawing.png"
```

**Response:**
```json
{
  "success": true,
  "design_id": "DS-2025-001",
  "message": "تم إرسال التصميم بنجاح"
}
```

### **📤 POST /upload-design**

رفع تصميم جاهز من صفحة الرفع.

**Request:**
```bash
curl -X POST http://localhost:5000/upload-design \
  -F "customerName=فاطمة علي" \
  -F "whatsapp=96599234567" \
  -F "serviceType=تنفيذ-حرفي" \
  -F "designFiles=@design1.jpg" \
  -F "designFiles=@design2.pdf"
```

**Response:**
```json
{
  "success": true,
  "design_id": "UD-2025-001",
  "message": "تم رفع التصميم بنجاح"
}
```

### **📊 GET /api/designs**

جلب جميع التصاميم (للإدارة).

**Response:**
```json
[
  {
    "design_id": "DS-2025-001",
    "customer_name": "أحمد محمد",
    "project_type": "مطبخ",
    "status": "completed",
    "timestamp": "2025-01-15T10:30:00Z",
    "whatsapp": "+965 9912 3456",
    "location": "حولي"
  }
]
```

### **🔍 GET /api/design/{id}**

جلب تفاصيل تصميم محدد.

**Response:**
```json
{
  "design_id": "DS-2025-001",
  "customer_name": "أحمد محمد",
  "whatsapp": "+965 9912 3456",
  "location": "حولي",
  "project_type": "مطبخ",
  "dimensions": {
    "width": "3.5",
    "height": "2.8"
  },
  "material": "LG",
  "status": "completed",
  "timestamp": "2025-01-15T10:30:00Z",
  "kitchenType": "مطبخ على شكل L",
  "sinkCount": "حوضين",
  "generated_image": "https://example.com/generated/DS-2025-001.jpg"
}
```

---

## 🛠️ **استكشاف الأخطاء**

### **🔥 مشاكل شائعة وحلولها**

#### **1. خطأ Replicate API**
```bash
ERROR: Replicate API authentication failed

✅ الحل:
- تحقق من صحة REPLICATE_API_TOKEN في .env
- تأكد من رصيد الحساب في Replicate
- جرب token جديد من الموقع
```

#### **2. فشل إرسال واتساب**
```bash
ERROR: WhatsApp message sending failed

✅ الحل:
- تحقق من إعدادات Twilio/WhatsApp API
- تأكد من تفعيل sandbox mode (للاختبار)
- فحص صحة أرقام الهاتف (+965 format)
```

#### **3. مشكلة رفع الملفات**
```bash
ERROR: File upload failed

✅ الحل:
- تحقق من أذونات مجلد uploads/
- زيادة MAX_CONTENT_LENGTH في .env
- فحص أنواع الملفات المدعومة
```

#### **4. خطأ في قاعدة البيانات**
```bash
ERROR: Database connection failed

✅ الحل:
- التحقق من وجود مجلد designs/
- إنشاء المجلدات المطلوبة:
  mkdir -p designs uploads generated_designs logs
```

### **🔍 فحص شامل للنظام**

```bash
# فحص حالة الخدمات
python -c "
import sys
import os
print('Python:', sys.version)
print('Working Directory:', os.getcwd())
print('Environment File:', os.path.exists('.env'))
print('Uploads Folder:', os.path.exists('uploads'))
print('Designs Folder:', os.path.exists('designs'))
"

# فحص المكتبات
pip list | grep -E "(flask|replicate|requests|pillow)"

# فحص الاتصال بـ APIs
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('Replicate Token:', 'Set' if os.getenv('REPLICATE_API_TOKEN') else 'Missing')
print('WhatsApp Config:', 'Set' if os.getenv('WHATSAPP_TOKEN') else 'Missing')
"
```

### **📋 نصائح التشخيص**

```bash
# تفعيل الوضع المفصل
export FLASK_ENV=development
export FLASK_DEBUG=True

# مراقبة السجلات المباشرة
tail -f logs/app.log | grep ERROR

# فحص استخدام الذاكرة
ps aux | grep python

# فحص المنافذ المستخدمة
netstat -tulpn | grep :5000
```

---

## 📊 **مراقبة الأداء**

### **📈 إحصائيات النظام**

#### **مراقبة مباشرة**
```bash
# فحص استخدام الموارد
htop

# مراقبة مساحة القرص
df -h

# فحص استخدام الذاكرة
free -h

# مراقبة العمليات
ps aux | grep python
```

#### **سجلات مفصلة**
```bash
# إحصائيات الطلبات
grep "submit-design" logs/app.log | wc -l

# الطلبات الناجحة
grep "success.*True" logs/app.log | wc -l

# الأخطاء
grep "ERROR" logs/app.log | tail -10

# أبطأ الطلبات
grep "processing time" logs/app.log | sort -k5 -nr | head -5
```

### **🔔 إعداد التنبيهات**

#### **تنبيهات البريد الإلكتروني** (اختياري)
```python
# إضافة للـ app.py
import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Corian Castle Alert'
    msg['From'] = 'alerts@corian-castle.com'
    msg['To'] = 'admin@corian-castle.com'
    
    server = smtplib.SMTP('localhost')
    server.send_message(msg)
    server.quit()
```

#### **مراقبة Uptime** (اختياري)
```bash
# إضافة crontab للفحص الدوري
crontab -e

# إضافة هذا السطر (فحص كل 5 دقائق)
*/5 * * * * curl -f http://localhost:5000/ || echo "Site Down" | mail -s "Alert" admin@corian-castle.com
```

### **📊 تقارير الأداء**

```python
# سكريبت تقرير يومي
# daily_report.py
import json
import os
from datetime import datetime, timedelta

def generate_daily_report():
    designs_dir = 'designs'
    today = datetime.now().date()
    
    # عدد الطلبات اليوم
    today_designs = []
    for filename in os.listdir(designs_dir):
        if filename.endswith('.json'):
            with open(os.path.join(designs_dir, filename)) as f:
                design = json.load(f)
                design_date = datetime.fromisoformat(design['timestamp']).date()
                if design_date == today:
                    today_designs.append(design)
    
    # إحصائيات
    total_today = len(today_designs)
    by_type = {}
    by_status = {}
    
    for design in today_designs:
        project_type = design.get('project_type', 'غير محدد')
        status = design.get('status', 'غير محدد')
        
        by_type[project_type] = by_type.get(project_type, 0) + 1
        by_status[status] = by_status.get(status, 0) + 1
    
    # طباعة التقرير
    print(f"📊 تقرير يومي - {today}")
    print(f"إجمالي الطلبات: {total_today}")
    print("\nحسب نوع المشروع:")
    for project_type, count in by_type.items():
        print(f"  {project_type}: {count}")
    print("\nحسب الحالة:")
    for status, count in by_status.items():
        print(f"  {status}: {count}")

if __name__ == "__main__":
    generate_daily_report()
```

---

## 🤝 **المساهمة**

نرحب بمساهماتكم لتطوير المشروع! 

### **🔄 خطوات المساهمة**

1. **Fork المشروع**
```bash
git clone https://github.com/your-username/corian-castle.git
cd corian-castle
```

2. **إنشاء branch جديد**
```bash
git checkout -b feature/amazing-feature
```

3. **إجراء التغييرات**
```bash
# تعديل الملفات
git add .
git commit -m "Add amazing feature"
```

4. **Push للـ branch**
```bash
git push origin feature/amazing-feature
```

5. **إنشاء Pull Request**

### **📋 معايير الكود**

```bash
# تحقق من جودة الكود
flake8 app.py
black app.py --check

# تشغيل الاختبارات
python -m pytest tests/

# فحص الأمان
bandit -r .
```

### **🧪 الاختبارات**

```python
# tests/test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_designer_page(self):
        response = self.app.get('/designer.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

### **🎯 مجالات المساهمة المطلوبة**

- **تحسين الواجهات** - UI/UX improvements
- **إضافة مميزات جديدة** - New features
- **تحسين الأداء** - Performance optimization
- **إضافة اختبارات** - Test coverage
- **تحسين الأمان** - Security enhancements
- **توثيق أفضل** - Documentation updates
- **إصلاح الأخطاء** - Bug fixes

---

## 📞 **الدعم التقني**

### **🆘 طرق الحصول على المساعدة**

#### **1. الدعم الفوري**
- 📧 **البريد الإلكتروني**: support@corian-castle.com
- 📱 **واتساب الدعم**: +965 9912 3456
- 💬 **شات مباشر**: متاح على الموقع 24/7

#### **2. المنتديات والمجتمع**
- 🐙 **GitHub Issues**: [Create Issue](https://github.com/your-repo/corian-castle/issues)
- 💬 **Discord Server**: [Join Community](https://discord.gg/corian-castle)
- 📚 **Stack Overflow**: Tag `corian-castle`

#### **3. الموارد التعليمية**
- 📹 **فيديوهات شرح**: [YouTube Channel](https://youtube.com/corian-castle)
- 📖 **مقالات تفصيلية**: [Blog](https://blog.corian-castle.com)
- 🎓 **دورات تدريبية**: متاحة للفرق التقنية

### **🔧 استكشاف المشاكل بنفسك**

#### **Quick Diagnostic Script**
```bash
#!/bin/bash
# quick_check.sh - فحص سريع للنظام

echo "🔍 فحص سريع لنظام كوريان كاسيل..."
echo "════════════════════════════════════════"

# فحص Python
python_version=$(python --version 2>&1)
echo "✓ Python: $python_version"

# فحص الملفات الأساسية
files=("app.py" ".env" "requirements.txt")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ $file: موجود"
    else
        echo "✗ $file: مفقود"
    fi
done

# فحص المجلدات
folders=("uploads" "designs" "generated_designs" "logs")
for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        echo "✓ $folder/: موجود"
    else
        echo "✗ $folder/: مفقود - يتم إنشاؤه..."
        mkdir -p "$folder"
    fi
done

# فحص المتغيرات
if [ -f ".env" ]; then
    echo "✓ ملف .env موجود"
    if grep -q "REPLICATE_API_TOKEN" .env; then
        echo "✓ Replicate API Token: مُعرَّف"
    else
        echo "✗ Replicate API Token: مفقود"
    fi
    
    if grep -q "WHATSAPP_TOKEN\|TWILIO_AUTH_TOKEN" .env; then
        echo "✓ WhatsApp API: مُعرَّف"
    else
        echo "✗ WhatsApp API: مفقود"
    fi
else
    echo "✗ ملف .env مفقود"
fi

# فحص المنفذ
if netstat -tuln | grep -q ":5000 "; then
    echo "✓ المنفذ 5000: مُستخدم (الخادم يعمل)"
else
    echo "ℹ المنفذ 5000: متاح"
fi

echo "════════════════════════════════════════"
echo "✅ انتهى الفحص السريع"
```

### **📋 قوالب البلاغات**

#### **🐛 تقرير خطأ**
```markdown
**وصف الخطأ**
وصف واضح ومختصر للخطأ.

**خطوات إعادة الإنتاج**
1. اذهب إلى '...'
2. انقر على '....'
3. قم بالتمرير لأسفل إلى '....'
4. شاهد الخطأ

**السلوك المتوقع**
وصف واضح ومختصر لما توقعت حدوثه.

**السلوك الفعلي**
وصف واضح ومختصر لما حدث فعلاً.

**لقطات الشاشة**
إذا كان مناسباً، أضف لقطات شاشة لمساعدتك في شرح مشكلتك.

**معلومات البيئة:**
- نظام التشغيل: [e.g. Ubuntu 20.04]
- Python Version: [e.g. 3.9.7]
- Browser: [e.g. chrome, safari]
- Version: [e.g. 22]

**معلومات إضافية**
أضف أي سياق آخر حول المشكلة هنا.
```

#### **💡 طلب ميزة جديدة**
```markdown
**هل طلبك متعلق بمشكلة؟ يرجى الوصف.**
وصف واضح ومختصر للمشكلة. مثال: أشعر بالإحباط عندما [...]

**صف الحل الذي تريده**
وصف واضح ومختصر لما تريده أن يحدث.

**صف البدائل التي فكرت فيها**
وصف واضح ومختصر لأي حلول أو ميزات بديلة فكرت فيها.

**سياق إضافي**
أضف أي سياق أو لقطات شاشة أخرى حول طلب الميزة هنا.
```

---

## 📈 **خارطة الطريق**

### **🎯 المرحلة الحالية - v1.0**
- ✅ التصميم التفاعلي الأساسي
- ✅ رفع التصاميم الجاهزة
- ✅ تكامل الذكاء الاصطناعي
- ✅ إرسال واتساب تلقائي
- ✅ لوحة تحكم إدارية

### **🚀 المرحلة القادمة - v1.1**
- 🔄 **نظام قاعدة بيانات** (PostgreSQL)
- 🔄 **نظام المصادقة** للمستخدمين
- 🔄 **معرض الأعمال** السابقة
- 🔄 **نظام التقييم** والمراجعات
- 🔄 **دردشة مباشرة** مع الدعم

### **🌟 المرحلة المستقبلية - v2.0**
- 🎯 **تطبيق موبايل** (React Native)
- 🎯 **نظام الدفع** الإلكتروني
- 🎯 **VR/AR Preview** للتصاميم
- 🎯 **ذكاء اصطناعي محسّن** (Custom Models)
- 🎯 **API عامة** للمطورين

### **🔮 الرؤية طويلة المدى - v3.0**
- 🌍 **توسع إقليمي** (دول الخليج)
- 🤖 **مساعد ذكي** بالصوت
- 🏭 **تكامل مع المصانع** (IoT)
- 📊 **تحليلات متقدمة** (Big Data)
- 🎨 **مولد تصاميم** ذاتي التعلم

---

## 🏆 **أمثلة ومشاريع مماثلة**

### **💼 مشاريع ملهمة**
- 🏠 **Houzz** - منصة تصميم المنازل
- 🛋️ **IKEA Place** - AR للأثاث
- 🎨 **SketchUp** - تصميم ثلاثي الأبعاد
- 🏗️ **AutoCAD Web** - تصميم معماري

### **🤖 تقنيات AI مستخدمة**
- **Replicate**: لتحويل الرسوم لتصاميم
- **Stable Diffusion**: لتوليد الصور
- **ControlNet**: للتحكم في الإخراج
- **CLIP**: لفهم النصوص والصور

### **📱 تكاملات محتملة**
- **WhatsApp Business API**
- **Twilio Programmable Messaging**
- **Google Vision API**
- **OpenAI GPT** للنصوص
- **Midjourney API** كبديل AI

---

## 📜 **الترخيص والحقوق**

### **📋 معلومات الترخيص**
```
MIT License

Copyright (c) 2025 Corian Castle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### **🔐 إقرار الأمان**
هذا المشروع مُصمم لأغراض تعليمية وتجارية. يرجى مراجعة إعدادات الأمان قبل النشر في بيئة الإنتاج.

### **⚖️ إخلاء المسؤولية**
- البرنامج مُقدم "كما هو" بدون ضمانات
- المطورون غير مسؤولين عن أي أضرار
- يُنصح بإجراء اختبارات شاملة قبل الاستخدام التجاري

---

## 🎉 **شكر وتقدير**

### **👥 الفريق الأساسي**
- **Lead Developer**: أحمد محمد
- **UI/UX Designer**: فاطمة علي  
- **AI Engineer**: خالد سعد
- **DevOps**: نورا أحمد

### **🙏 شكر خاص**
- **كوريان كاسيل** - للفكرة والدعم
- **مجتمع Flask** - للمكتبات الرائعة
- **Replicate** - لتقنية الذكاء الاصطناعي
- **المساهمين** - لجعل المشروع أفضل

### **📚 مصادر الإلهام**
- **Material Design** - نظام التصميم
- **Arabic Web Typography** - الخطوط العربية
- **Kuwait Design Heritage** - التراث الكويتي
- **Modern Architecture** - العمارة الحديثة

---

## 📞 **تواصل معنا**

### **🏢 معلومات الشركة**
```
كوريان كاسيل
رواد تصنيع وتشكيل الكوريان بالكويت

📍 العنوان: شارع الخليج العربي، مدينة الكويت
📱 الهاتف: +965 2222 3333
📲 واتساب: +965 9912 3456
📧 البريد: info@corian-castle.com
🌐 الموقع: https://corian-castle.com
```

### **💻 التطوير التقني**
```
📧 الدعم التقني: dev@corian-castle.com
🐙 GitHub: https://github.com/corian-castle
💬 Discord: https://discord.gg/corian-castle
📚 Documentation: https://docs.corian-castle.com
```

### **📱 وسائل التواصل**
```
📘 Facebook: /CorianCastleKuwait
📸 Instagram: @corian_castle_kw
🐦 Twitter: @CorianCastleKW
💼 LinkedIn: /company/corian-castle
🎬 YouTube: /CorianCastleKuwait
```

---

<div align="center">

### **✨ شكراً لاستخدام منصة كوريان كاسيل! ✨**

**"الخيال عليك ... والواقع علينا"**

---

[![GitHub Stars](https://img.shields.io/github/stars/corian-castle/corian-castle?style=social)](https://github.com/corian-castle/corian-castle)
[![Follow on Twitter](https://img.shields.io/twitter/follow/CorianCastleKW?style=social)](https://twitter.com/CorianCastleKW)

**صنع بـ ❤️ في الكويت 🇰🇼**

</div>