# Adım 1: Temel Python imajını kullan
FROM python:3.9-slim

# Adım 2: Çalışma dizinini ayarla
WORKDIR /app

# Adım 3: Gereksinimleri kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Adım 4: Proje dosyalarını kopyala
COPY . .

# Adım 5: Portu aç ve uygulamayı Gunicorn ile başlat
# Render, varsayılan olarak 10000 portunu kullanmayı sever.
EXPOSE 10000
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "api_app:app"]