import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

def main():
    """
    Program utama yang mengimplementasikan analisis data sederhana
    menggunakan struktur kontrol, struktur data, dan beberapa library.
    """
    print("=== PROGRAM ANALISIS DATA SEDERHANA ===")
    print("Program ini akan membantu Anda menganalisis data numerik sederhana.")
    
    # Struktur data - list untuk menyimpan nilai input dari pengguna
    data_values = []
    
    # Struktur kontrol - loop untuk input data
    while True:
        try:
            # Input dari pengguna
            user_input = input("\nMasukkan nilai numerik (atau 'selesai' untuk mengakhiri input): ")
            
            # Struktur kontrol - kondisional untuk memeriksa input
            if user_input.lower() == 'selesai':
                if len(data_values) == 0:
                    print("Anda belum memasukkan data. Mohon masukkan minimal 1 data.")
                    continue
                break
            
            # Konversi input ke float dan tambahkan ke list
            value = float(user_input)
            data_values.append(value)
            print(f"Nilai {value} telah ditambahkan ke data.")
            
        except ValueError:
            print("Input tidak valid. Masukkan angka atau 'selesai'.")
    
    # Menggunakan numpy untuk analisis statistik
    data_array = np.array(data_values)
    
    # Struktur kontrol - if-else untuk menampilkan hasil analisis
    if len(data_array) > 0:
        mean_value = np.mean(data_array)
        median_value = np.median(data_array)
        std_dev = np.std(data_array)
        max_value = np.max(data_array)
        min_value = np.min(data_array)
        
        # Menampilkan hasil analisis
        print("\n=== HASIL ANALISIS DATA ===")
        print(f"Data: {data_values}")
        print(f"Jumlah data: {len(data_values)}")
        print(f"Nilai rata-rata: {mean_value:.2f}")
        print(f"Nilai tengah (median): {median_value:.2f}")
        print(f"Deviasi standar: {std_dev:.2f}")
        print(f"Nilai maksimum: {max_value:.2f}")
        print(f"Nilai minimum: {min_value:.2f}")
        
        # Struktur data - dictionary untuk menyimpan hasil analisis
        analysis_results = {
            'data': data_values,
            'mean': mean_value,
            'median': median_value,
            'std_dev': std_dev,
            'max': max_value,
            'min': min_value,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Visualisasi data menggunakan matplotlib
        print("\nMembuat visualisasi data...")
        
        # Membuat folder output jika belum ada
        if not os.path.exists('output'):
            os.makedirs('output')
        
        # Membuat histogram
        plt.figure(figsize=(10, 6))
        plt.hist(data_array, bins=min(10, len(data_array)), alpha=0.7, color='skyblue', edgecolor='black')
        plt.title('Histogram Data')
        plt.xlabel('Nilai')
        plt.ylabel('Frekuensi')
        plt.grid(axis='y', alpha=0.75)
        plt.savefig('output/histogram.png')
        
        # Membuat plot garis
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(data_array)), sorted(data_array), marker='o', linestyle='-', color='green')
        plt.title('Plot Nilai Data (Terurut)')
        plt.xlabel('Indeks')
        plt.ylabel('Nilai')
        plt.grid(True)
        plt.savefig('output/line_plot.png')
        
        # Membuat boxplot
        plt.figure(figsize=(8, 6))
        plt.boxplot(data_array, vert=True, patch_artist=True)
        plt.title('Boxplot Data')
        plt.ylabel('Nilai')
        plt.grid(axis='y', alpha=0.75)
        plt.savefig('output/boxplot.png')
        
        print("Visualisasi telah disimpan dalam folder 'output'.")
        
        # Menyimpan hasil analisis ke CSV menggunakan pandas
        df = pd.DataFrame([analysis_results])
        df.to_csv('output/analysis_results.csv', index=False)
        print("Hasil analisis telah disimpan dalam file 'output/analysis_results.csv'.")
        
    else:
        print("Tidak ada data untuk dianalisis.")

if __name__ == "__main__":
    main()