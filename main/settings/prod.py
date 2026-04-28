from .base import *
import dj_database_url

DEBUG = False # Production'da kesinlikle False!

# Railway'in vereceği domain'i buraya ekleyeceğiz, şimdilik her şeye izin verelim
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*").split(",")
 
# Neon PostgreSQL ayarıları, Railway'de de benzer şekilde çalışır
DATABASES = { 
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="postgres://user:pass@localhost:5432/db_name"), # Railway'deki bağlantı dizesi
        conn_max_age=600,
        conn_health_checks=True,
    )
} 

# CSRF hatasını çözmek için Railway linkini buraya ekliyoruz
CSRF_TRUSTED_ORIGINS = [
    "https://flight-reservation-api-production.up.railway.app"
]

# Statik dosyalar için WhiteNoise ayarı
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Django'nun Railway/Proxy arkasında olduğunu anlamasını sağlar
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Tüm HTTP isteklerini HTTPS'e yönlendirir
SECURE_SSL_REDIRECT = True

# Session ve CSRF çerezlerini sadece HTTPS üzerinden gönderir
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True