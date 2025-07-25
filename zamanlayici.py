import schedule
import time
from datetime import datetime
import pandas as pd
import numpy as np
import joblib

# --- 1. Veri Ön İşleme Fonksiyonu ---
def on_isle(df, train_columns):
    """Gelen ham veriyi modele uygun hale getiren fonksiyon."""
    df['Tarih'] = pd.to_datetime(df['Tarih'])
    df['Yıl'] = df['Tarih'].dt.year
    df['Ay'] = df['Tarih'].dt.month
    df['Gün'] = df['Tarih'].dt.day
    df['Haftanın_Günü'] = df['Tarih'].dt.day_name()
    df.drop('Tarih', axis=1, inplace=True)
    df['Detay_Karakter_Sayısı'] = df['Detay'].apply(len)
    df['Detay_Kelime_Sayısı'] = df['Detay'].apply(lambda x: len(str(x).split()))
    df['Detay_Cukur_Var'] = df['Detay'].apply(lambda x: 1 if 'çukur' in str(x).lower() else 0)
    df.drop(['ID', 'Detay', 'Çözüm_süresi_gün'], axis=1, inplace=True, errors='ignore')
    categorical_cols = ['İlçe', 'Kategori', 'Kanal', 'Çözüm_Durumu', 'Haftanın_Günü']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    missing_cols = set(train_columns) - set(df.columns)
    for c in missing_cols:
        df[c] = 0
    df = df[train_columns]
    return df

# --- 2. Ana Görev Fonksiyonu ---
def gunluk_analiz_gorevi():
    """Günlük olarak çalıştırılacak ana görev."""
    print(f"{datetime.now()}: Günlük analiz görevi başlatıldı.")
    try:
        df_yeni = pd.read_csv('yeni_sikayetler.csv')
        print(f"{len(df_yeni)} adet yeni şikayet bulundu.")
        model = joblib.load('cozum_suresi_modeli.pkl')
        train_columns = joblib.load('egitim_sutunlari.pkl')
        df_islenmis = on_isle(df_yeni.copy(), train_columns)
        tahminler = model.predict(df_islenmis)
        df_yeni['Tahmin_Edilen_Cozum_Suresi_Gun'] = np.round(tahminler, 1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"tahmin_sonuclari_{timestamp}.csv"
        df_yeni.to_csv(output_filename, index=False)
        print(f"Sonuçlar '{output_filename}' dosyasına kaydedildi.")
    except FileNotFoundError:
        print("HATA: Gerekli dosyalar ('yeni_sikayetler.csv', 'cozum_suresi_modeli.pkl' veya 'egitim_sutunlari.pkl') bulunamadı.")
    except Exception as e:
        print(f"Görev sırasında bir hata oluştu: {e}")
    finally:
        print(f"{datetime.now()}: Görev tamamlandı.\n" + "-"*40)

# --- 3. Zamanlayıcı Kurulumu ---
schedule.every().day.at("09:00").do(gunluk_analiz_gorevi)
print("Zamanlayıcı başlatıldı. Görevlerin çalışması için bekleniyor...")
while True:
    schedule.run_pending()
    time.sleep(1)```
**Çıktısı:**
