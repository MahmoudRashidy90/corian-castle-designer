#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Passenger WSGI للنشر على الخادم
"""

import sys
import os

# إضافة المجلد الحالي لمسار Python
sys.path.insert(0, os.path.dirname(__file__))

try:
    # استيراد التطبيق من app.py
    from app import application
    print("✅ Passenger: تم تحميل التطبيق بنجاح")
    
except ImportError as e:
    print(f"❌ Passenger: خطأ في استيراد التطبيق - {e}")
    raise
    
except Exception as e:
    print(f"❌ Passenger: خطأ عام - {e}")
    raise