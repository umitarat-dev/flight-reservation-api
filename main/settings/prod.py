from .base import *
import dj_database_url

DEBUG = False # Production'da kesinlikle False!

# Railway'in vereceği domain'i buraya ekleyeceğiz, şimdilik her şeye izin verelim
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*").split(",")
 
# Neon PostgreSQL ayarıları, Railway'de de benzer şekilde çalışır
DATABASES = { 
    "default": dj_database_url.config(
        default=config("DATABASE_URL"), # Railway'deki bağlantı dizesi
        conn_max_age=600,
        conn_health_checks=True,
    )
} 

# Statik dosyalar için WhiteNoise ayarı
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'