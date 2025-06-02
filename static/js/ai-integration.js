// AI Integration - آمن ومختصر
(function() {
    'use strict';
    
    console.log('🤖 AI Integration Loading...');
    
    let isGenerating = false;
    
    // تحميل الصفحة
    document.addEventListener('DOMContentLoaded', function() {
        addAISection();
        addAIStyles();
    });
    
    // إضافة الـ CSS
    function addAIStyles() {
        if (document.getElementById('ai-styles')) return;
        
        const style = document.createElement('style');
        style.id = 'ai-styles';
        style.textContent = `
            .ai-section {
                background: linear-gradient(135deg, rgba(196, 150, 90, 0.15), rgba(196, 150, 90, 0.05));
                border: 2px solid rgba(196, 150, 90, 0.4);
                border-radius: 20px;
                padding: 30px;
                margin: 30px 0;
                text-align: center;
            }
            .ai-prompt {
                width: 100%;
                padding: 18px;
                background: rgba(255, 255, 255, 0.12);
                border: 2px solid rgba(196, 150, 90, 0.4);
                border-radius: 15px;
                color: #fff;
                margin: 20px 0;
                min-height: 120px;
                resize: vertical;
            }
            .ai-generate-btn {
                background: linear-gradient(45deg, #C4965A, #D4A574);
                color: #1a1a1a;
                border: none;
                padding: 20px 50px;
                border-radius: 50px;
                font-size: 1.3rem;
                font-weight: bold;
                cursor: pointer;
            }
            .ai-result {
                margin-top: 30px;
                padding: 25px;
                background: rgba(255, 255, 255, 0.08);
                border-radius: 15px;
                display: none;
            }
            .ai-result.show { display: block; }
            .ai-generated-image {
                max-width: 100%;
                border-radius: 15px;
                margin: 15px 0;
            }
        `;
        document.head.appendChild(style);
    }
    
    // إضافة قسم الـ AI
    function addAISection() {
        const formContainer = document.querySelector('.form-container');
        if (!formContainer) return;
        
        const aiSection = document.createElement('div');
        aiSection.className = 'ai-section';
        aiSection.innerHTML = `
            <h3 style="color: #C4965A; margin-bottom: 15px;">🤖 مولد التصاميم بالذكاء الاصطناعي</h3>
            <p style="color: rgba(255,255,255,0.9); margin-bottom: 25px;">اكتب وصف تصميمك وسنحوله لصورة واقعية</p>
            
            <textarea 
                class="ai-prompt" 
                id="aiPrompt"
                placeholder="مثال: مطبخ عصري بكاونتر كوريان أبيض لامع، خزائن رمادية، إضاءة LED"
                rows="4"
            ></textarea>
            
            <button class="ai-generate-btn" id="aiGenerateBtn" onclick="generateAIDesign()">
                <i class="fas fa-magic"></i> ولّد التصميم
            </button>
            
            <div class="ai-result" id="aiResult">
                <div id="aiImageContainer"></div>
            </div>
        `;
        
        formContainer.insertBefore(aiSection, formContainer.firstChild);
    }
    
    // ✅ الدالة الآمنة - استخدام backend فقط
    window.generateAIDesign = function() {
        if (isGenerating) return;
        
        const promptInput = document.getElementById('aiPrompt');
        const generateBtn = document.getElementById('aiGenerateBtn');
        const resultDiv = document.getElementById('aiResult');
        const imageContainer = document.getElementById('aiImageContainer');
        
        if (!promptInput?.value?.trim()) {
            alert('يرجى إدخال وصف للتصميم');
            return;
        }
        
        if (promptInput.value.trim().length < 10) {
            alert('الوصف قصير جداً، اكتب تفاصيل أكثر');
            return;
        }
        
        isGenerating = true;
        generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري التوليد...';
        generateBtn.disabled = true;
        resultDiv.classList.remove('show');
        
        // ✅ استدعاء backend API الآمن
        fetch('/api/generate-ai', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                prompt: promptInput.value.trim(),
                width: 768,
                height: 768
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showResult(data.image_url, data.filename);
            } else {
                showError(data.error || 'حدث خطأ في التوليد');
            }
        })
        .catch(error => {
            console.error('AI Error:', error);
            showFallbackResult(promptInput.value.trim());
        })
        .finally(() => {
            resetUI();
        });
    };
    
    function showResult(imageUrl, filename) {
        const imageContainer = document.getElementById('aiImageContainer');
        const resultDiv = document.getElementById('aiResult');
        
        imageContainer.innerHTML = `
            <h4 style="color: #C4965A; margin-bottom: 20px;">✨ تصميمك جاهز!</h4>
            <img src="${imageUrl}" alt="التصميم المولد" class="ai-generated-image">
            <div style="margin-top: 20px;">
                <button onclick="downloadImage('${imageUrl}', '${filename}')" style="background: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 25px; margin: 5px; cursor: pointer;">
                    📥 تحميل
                </button>
                <button onclick="shareWhatsApp('${imageUrl}')" style="background: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 25px; margin: 5px; cursor: pointer;">
                    📱 شارك
                </button>
                <button onclick="tryAgain()" style="background: #6c757d; color: white; border: none; padding: 10px 20px; border-radius: 25px; margin: 5px; cursor: pointer;">
                    🔄 جرب مرة أخرى
                </button>
            </div>
        `;
        
        resultDiv.classList.add('show');
        console.log('✅ AI generation successful');
    }
    
    function showFallbackResult(prompt) {
        const imageContainer = document.getElementById('aiImageContainer');
        const resultDiv = document.getElementById('aiResult');
        
        // صور احتياطية حسب النوع
        const fallbackImages = {
            'مطبخ': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&h=400&fit=crop',
            'مغسلة': 'https://images.unsplash.com/photo-1620626011761-996317b8d101?w=600&h=400&fit=crop',
            'default': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=600&h=400&fit=crop'
        };
        
        const projectType = getProjectType();
        const imageUrl = fallbackImages[projectType] || fallbackImages.default;
        
        imageContainer.innerHTML = `
            <div style="background: rgba(255,191,36,0.15); padding: 15px; border-radius: 10px; margin-bottom: 15px;">
                <strong>⚠️ وضع احتياطي:</strong> عرض صورة مقترحة - سيتم تفعيل AI قريباً
            </div>
            <h4 style="color: #C4965A; margin-bottom: 15px;">💡 تصميم مقترح لـ: "${prompt}"</h4>
            <img src="${imageUrl}" alt="تصميم مقترح" class="ai-generated-image">
            <div style="margin-top: 20px;">
                <button onclick="tryAgain()" style="background: #C4965A; color: white; border: none; padding: 10px 20px; border-radius: 25px; cursor: pointer;">
                    🔄 جرب مرة أخرى
                </button>
            </div>
        `;
        
        resultDiv.classList.add('show');
        console.log('⚠️ Showing fallback result');
    }
    
    function showError(message) {
        const imageContainer = document.getElementById('aiImageContainer');
        const resultDiv = document.getElementById('aiResult');
        
        imageContainer.innerHTML = `
            <div style="background: rgba(244, 67, 54, 0.15); padding: 15px; border-radius: 10px; color: #ff6b6b;">
                <strong>❌ خطأ:</strong> ${message}
            </div>
            <button onclick="tryAgain()" style="background: #C4965A; color: white; border: none; padding: 10px 20px; border-radius: 25px; margin-top: 15px; cursor: pointer;">
                🔄 حاول مرة أخرى
            </button>
        `;
        
        resultDiv.classList.add('show');
    }
    
    function resetUI() {
        isGenerating = false;
        const generateBtn = document.getElementById('aiGenerateBtn');
        if (generateBtn) {
            generateBtn.innerHTML = '<i class="fas fa-magic"></i> ولّد التصميم';
            generateBtn.disabled = false;
        }
    }
    
    function getProjectType() {
        const select = document.getElementById('projectType');
        return select?.value || 'مطبخ';
    }
    
    // دوال مساعدة
    window.downloadImage = function(url, filename) {
        const link = document.createElement('a');
        link.href = url;
        link.download = filename || `corian-design-${Date.now()}.jpg`;
        link.click();
    };
    
    window.shareWhatsApp = function(imageUrl) {
        const message = `🎨 شوف التصميم الجديد من كوريان كاسيل!\n📸 ${imageUrl}`;
        window.open(`https://wa.me/?text=${encodeURIComponent(message)}`);
    };
    
    window.tryAgain = function() {
        document.getElementById('aiResult').classList.remove('show');
        document.getElementById('aiPrompt').focus();
    };
    
})();