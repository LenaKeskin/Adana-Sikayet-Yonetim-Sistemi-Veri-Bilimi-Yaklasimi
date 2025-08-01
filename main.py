import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Veri dosyasının yolu
    data_path = os.path.join(os.path.dirname(__file__), 'your_data.csv')

    # Veriyi yükle
    data = pd.read_csv(data_path)

    # Grafik: Eğitim Seviyesi Dağılımı
    plt.figure(figsize=(10,6))
    sns.countplot(data=data, x="education_level")
    plt.title("Eğitim Seviyesi Dağılımı")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Çıktı klasörü varsa kullan, yoksa oluştur
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'education_plot.png')
    plt.savefig(output_file)

    print(f"Grafik başarıyla oluşturuldu ve kaydedildi: {output_file}")

if __name__ == "__main__":
    main()
