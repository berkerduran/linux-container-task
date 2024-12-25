# Python 3 tabanlı bir temel imaj kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app
# Uygulama dosyasını kopyala
COPY app.py /app/

# Uygulamayı başlat
CMD ["python", "app.py"]

# Portu dışarı aç (8000 portu)
EXPOSE 8000
