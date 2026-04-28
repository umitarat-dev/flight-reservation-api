# Python 3.11 tabanlı hafif bir imaj kullanıyoruz
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Python çıktılarını terminale anlık basması için ayar
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Sistem bağımlılıklarını yükle (psycopg2 ve diğerleri için)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Statik dosyaları topla (prod.py ayarları sayesinde)
RUN python manage.py collectstatic --noinput --settings=main.settings.prod

# Uygulamayı gunicorn ile 8080 portundan ayağa kaldır
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main.wsgi:application"]