# Adana-Sikayet-Yonetim-Sistemi-Veri-Bilimi-Yaklasimi

## Proje Hakkında
Bu proje, vatandaşlardan gelen şikayet verilerinin toplanması, analizi ve raporlanmasını amaçlayan kapsamlı bir veri analizi sistemidir. Projede Python tabanlı veri işleme, makine öğrenmesi modelleri, Power BI görselleştirmeleri ve Flask ile web arayüzü entegrasyonu yapılmıştır.

---

## Kullanılan Teknolojiler
- **Python** (pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost)
- **Flask** (Web API ve kullanıcı arayüzü için)
- **Power BI** (Veri görselleştirme)
- **FPDF** (PDF rapor oluşturma)
- **JSON** (Veri saklama formatı)
- **Git & GitHub** (Versiyon kontrol)
- **Docker** (Opsiyonel, konteynerleştirme için)

---

## Proje Özellikleri

### Veri İşleme ve Analiz
- JSON formatında şikayet verilerinin okunması ve ön işlenmesi
- Eksik veri temizliği ve veri dönüşümleri
- Yeni özelliklerin (feature engineering) eklenmesi
- Kategorik verilerin analizi ve görselleştirilmesi

### Makine Öğrenmesi Modelleri
- Karar Ağaçları (Decision Tree)
- Random Forest
- XGBoost  
Yukarıdaki modeller kullanılarak şikayetlerin çözüm durumları tahmin edilmiştir. Modellerin karşılaştırılması ve performans değerlendirmesi yapılmıştır.

### Web Arayüzü ve API
- Flask ile tam entegre çalışan web uygulaması
- Şikayet ekleme, güncelleme ve listeleme API'ları
- Kullanıcı dostu HTML form ve dinamik tablo gösterimi
- PDF formatında rapor oluşturma ve indirme özelliği

### Raporlama ve Bildirimler
- Grafikler ve istatistiklerle zenginleştirilmiş PDF raporlar
- Power BI dashboard ile etkileşimli görselleştirmeler

### Otomasyon ve Süreç Yönetimi
- Veri güncellemeleri için zamanlanmış görevler (opsiyonel)
- Loglama ve hata yönetimi (planlanıyor)

---

## Kurulum ve Çalıştırma

1. Depoyu klonlayın veya ZIP olarak indirin:
   ```bash
   git clone https://github.com/LenaKeskin/Adana-Sikayet-Yonetim-Sistemi-Veri-Bilimi-Yaklasimi
.git
   cd projeAdi
