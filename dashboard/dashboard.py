import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set up the page
st.title("Proyek Analisis Data: Bike Sharing Dataset")

# Data Wrangling
st.header("Pengolahan Data")

# Gathering Data
st.subheader("Memuat Data")
day_data = pd.read_csv('data/day.csv')
hour_data = pd.read_csv('data/hour.csv')

# Assesing Data
st.subheader("Tampilan Awal Data")
st.write("Data Harian:")
st.dataframe(day_data.head())

st.write("Data Per Jam:")
st.dataframe(hour_data.head())

# Cleaning Data
st.subheader("Pembersihan Data")
st.write("Mengonversi kolom 'dteday' menjadi tipe datetime.")
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Exploratory Data Analysis (EDA)
st.header("Analisis Data Eksploratif")

# Analisis Kolerasi antar fitur.
st.subheader("Korelasi Antar Fitur")
numeric_columns = day_data.select_dtypes(include=['number'])
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Heatmap Korelasi Antar Fitur')
st.pyplot(plt)

# Visualization & Explanatory Analysis
st.header("Visualisasi dan Analisis Penjelasan")

# Pertanyaan 1: Bagaimana Pengaruh Cuaca dan Musim Terhadap Jumlah Penyewaan Sepeda?
st.subheader("Pengaruh Cuaca dan Musim Terhadap Jumlah Penyewaan Sepeda")
weather_season_grouped = day_data.groupby(['weathersit', 'season']).agg({'cnt': 'mean'}).reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='weathersit', y='cnt', hue='season', data=weather_season_grouped)
plt.title('Rata-Rata Jumlah Penyewaan Sepeda Berdasarkan Cuaca dan Musim')
plt.xlabel('Situasi Cuaca')
plt.ylabel('Rata-Rata Jumlah Penyewaan')
st.pyplot(plt)

# Pertanyaan 2: Pada Jam Berapa Penyewaan Sepeda Terjadi Paling Banyak?
st.subheader("Jam-Jam Sibuk Penyewaan Sepeda")
hour_grouped = hour_data.groupby('hr').agg({'cnt': 'mean'}).reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='hr', y='cnt', data=hour_grouped, palette='Blues_d')
plt.title('Rata-Rata Jumlah Penyewaan Sepeda Berdasarkan Jam')
plt.xlabel('Jam dalam Sehari')
plt.ylabel('Rata-Rata Jumlah Penyewaan')
st.pyplot(plt)

# Conclusion
st.header("Kesimpulan")

st.subheader("Kesimpulan Pertanyaan 1")
st.write("Cuaca dan musim mempengaruhi jumlah penyewaan sepeda, dengan cuaca yang lebih baik dan musim yang lebih hangat meningkatkan jumlah penyewaan.")

st.subheader("Kesimpulan Pertanyaan 2")
st.write("Jam sibuk penyewaan sepeda terjadi pada pagi hari sekitar jam 8 dan sore hari sekitar jam 17, yang kemungkinan besar terkait dengan waktu berangkat dan pulang kerja.")
