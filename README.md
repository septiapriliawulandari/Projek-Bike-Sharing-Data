# Bike Sharing Analysis Project

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda berdasarkan kondisi cuaca, musim, dan waktu, serta mengeksplorasi faktor-faktor lingkungan yang mempengaruhi jumlah penyewaan sepeda.

## Table of Contents
1. [Tujuan Proyek](#tujuan-proyek)
2. [Struktur Proyek](#struktur-proyek)
3. [Cara Menjalankan Proyek](#cara-menjalankan-proyek)
4. [Pertanyaan Bisnis](#pertanyaan-bisnis)
5. [Analisis Data](#analisis-data)
6. [Kesimpulan](#kesimpulan)
7. [Sumber Data](#sumber-data)

## Tujuan Proyek
Tujuan dari proyek ini adalah untuk mengidentifikasi dan menganalisis faktor-faktor yang mempengaruhi jumlah penyewaan sepeda di suatu kota. Dengan menggunakan dataset yang tersedia, kami mencoba menjawab pertanyaan bisnis dan memberikan insight yang berguna untuk pengambilan keputusan.

## Struktur Proyek
- `data/`: Folder ini berisi dataset yang digunakan dalam proyek.
  - `day.csv`: Data penyewaan sepeda harian.
  - `hour.csv`: Data penyewaan sepeda per jam.
- `src/`: Folder ini berisi kode sumber untuk analisis data dan pembuatan dashboard.
  - `main.py`: Kode untuk menjalankan aplikasi dashboard Streamlit.
- `README.md`: File ini, yang menjelaskan proyek dan cara menggunakannya.
- `requirements.txt`: Daftar semua dependensi yang diperlukan untuk menjalankan proyek.
- `notebooks/`: Folder ini berisi notebook Jupyter yang digunakan untuk eksplorasi dan analisis data.

## Cara Menjalankan Proyek
### Persyaratan Sistem
Pastikan Anda telah menginstal:
- Python 3.7 atau versi lebih baru
- pip (Python package manager)

### Instalasi
1. Instal semua dependensi yang diperlukan:
    pandas
    numpy
    matplotlib
    seaborn
    streamlit
    menggunakan kode dibawah ini
   ```bash
   pip install -r requirements.txt

2. Instal Jupyter Notebook menggunakan pip
    ```bash
    pip install notebook

### Jalankan aplikasi Streamlit
1. Jalankan aplikasi Streamlit
    ```bash
    streamlit run dashboard/dashboard.py

### Menjalankan Analisis di Jupyter Notebook
1. Menjalankan Analisis di Jupyter Notebook
    ```bash
    jupyter notebook