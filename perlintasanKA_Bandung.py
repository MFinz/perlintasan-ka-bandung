import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Judul
st.title("Perlintasan Kereta Api di Bandung")



# Titik peta
center_lat = -6.9172
center_lot = 107.6208

# Daftar Perlintasan Kereta Api di Bandung
df = pd.read_excel('lokasi_perlintasan_bandung.xlsx')

# Modifikasi nomor biar dimulai dari 1
df_tampil = df.copy()
df_tampil.index = df_tampil.index + 1

# Menampilkan Data Scraping
with st.expander("Data Mentah (Bukan Hasil Scraping)"):
    st.write("Ini adalah data yang aku buat sendiri")
    st.dataframe(df_tampil)

# Buat kanvas (grafik)
fig, ax = plt.subplots(figsize=(8, 8))

# Hitung jumlah kategori 
counts = df['kategori'].value_counts()

ax.pie(
    counts.values,
    labels=counts.index,
    autopct = '%1.1f%%',
    startangle = 90,
    colors = plt.cm.Pastel1.colors
)

ax.axis('equal')

# Judul grafik
plt.title("Macam-Macam Tipe Perlintasan KA", fontsize=14)

# Buat peta
m = folium.Map(location=[center_lat, center_lot], zoom_start = 13)

# Marker Semua Perlintasan KA
for index, row in df.iterrows():
    folium.Marker(
    location = [row['lat'], row['lon']],
    tooltip = row['nama_lokasi'],
    popup = row['nama_lokasi'],
    icon =folium.Icon(color="blue", icon="train", prefix="fa")
    ).add_to(m)

# Tampil di Streamlit
st.subheader("Peta Perlintasan KA")
st_folium(m, height=500, width=800)

# Judul Pie Chart
st.subheader("Data Penting Mengenai Perlintasan KA")
st.pyplot(fig)

# Simpan ke HTML
# m.save("peta_coba.html")
# print("Peta berhasil dibuat!")


