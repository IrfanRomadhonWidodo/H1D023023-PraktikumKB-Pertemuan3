# NIM-PraktikumKB-Pertemuan3

## Analisis Data Sederhana dengan Python

Program analisis data sederhana yang mengimplementasikan konsep struktur kontrol, struktur data, dan berbagai library Python.

### Prasyarat

Sebelum menjalankan program ini, pastikan Anda telah menginstal library yang diperlukan:

```bash
pip install numpy matplotlib pandas
```

### Deskripsi

Program ini adalah aplikasi analisis data sederhana yang memungkinkan pengguna untuk:

1. Memasukkan serangkaian nilai numerik
2. Melakukan analisis statistik dasar (rata-rata, median, standar deviasi, nilai maksimum dan minimum)
3. Membuat visualisasi data dalam bentuk histogram, plot garis, dan boxplot
4. Menyimpan hasil analisis dalam format CSV

### Fitur

- ✅ Input data interaktif melalui command line
- ✅ Validasi input untuk memastikan data yang valid
- ✅ Analisis statistik menggunakan NumPy
- ✅ Visualisasi data menggunakan Matplotlib
- ✅ Penyimpanan hasil menggunakan Pandas

### Implementasi Konsep

#### 1. Struktur Kontrol

- Penggunaan loop `while` untuk input data berulang
- Penggunaan kondisional `if-else` untuk validasi input dan alur program
- Penggunaan `try-except` untuk penanganan error

#### 2. Struktur Data

- Penggunaan `list` untuk menyimpan nilai input dari pengguna
- Penggunaan `dictionary` untuk menyimpan hasil analisis
- Penggunaan array NumPy untuk komputasi statistik
- Penggunaan DataFrame Pandas untuk ekspor data

#### 3. Library

Program ini menggunakan empat library Python:

- **NumPy** - untuk analisis statistik
- **Matplotlib** - untuk visualisasi data
- **Pandas** - untuk manipulasi dan ekspor data
- **os** dan **datetime** - untuk manajemen file dan timestamp

### Cara Menggunakan

1. Clone repositori ini:

   ```bash
   git clone https://github.com/IrfanRomadhonWidodo/H1D023023-PraktikumKB-Pertemuan3.git
   cd H1D023023-PraktikumKB-Pertemuan3
   ```

2. Pastikan library yang diperlukan sudah terinstal:

   ```bash
   pip install numpy matplotlib pandas
   ```

3. Jalankan program:

   ```bash
   python main.py
   ```

4. Ikuti instruksi untuk memasukkan nilai numerik:

   - Masukkan angka satu per satu
   - Ketik 'selesai' untuk mengakhiri input dan melihat hasil analisis

5. Hasil visualisasi akan disimpan dalam folder 'output':

   - histogram.png
   - line_plot.png
   - boxplot.png

6. Hasil analisis akan disimpan dalam file 'output/analysis_results.csv'

### Struktur Folder

```
H1D023023-PraktikumKB-Pertemuan3/
├── main.py          # File program utama
├── README.md        # Dokumentasi program
└── output/          # Folder output (dibuat otomatis)
    ├── histogram.png
    ├── line_plot.png
    ├── boxplot.png
    └── analysis_results.csv
```

### Contoh Output

```
=== PROGRAM ANALISIS DATA SEDERHANA ===
Program ini akan membantu Anda menganalisis data numerik sederhana.

Masukkan nilai numerik (atau 'selesai' untuk mengakhiri input): 10
Nilai 10.0 telah ditambahkan ke data.

Masukkan nilai numerik (atau 'selesai' untuk mengakhiri input): 15
Nilai 15.0 telah ditambahkan ke data.

Masukkan nilai numerik (atau 'selesai' untuk mengakhiri input): 20
Nilai 20.0 telah ditambahkan ke data.

Masukkan nilai numerik (atau 'selesai' untuk mengakhiri input): selesai

=== HASIL ANALISIS DATA ===
Data: [10.0, 15.0, 20.0]
Jumlah data: 3
Nilai rata-rata: 15.00
Nilai tengah (median): 15.00
Deviasi standar: 4.08
Nilai maksimum: 20.00
Nilai minimum: 10.00

Membuat visualisasi data...
Visualisasi telah disimpan dalam folder 'output'.
Hasil analisis telah disimpan dalam file 'output/analysis_results.csv'.
```

### Author

**[Irfan Romadhon Widodo]**  
NIM: [H1D023023]
