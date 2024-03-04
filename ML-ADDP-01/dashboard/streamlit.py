import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


sns.set(style='dark')

bike_day = pd.read_csv("../ML-ADDP-01/Bike-sharing-dataset/day.csv")

# menambah label pada season
season_labels = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',  # Mengoreksi label Fall
    4: 'Winter'
}

bike_day['season_label'] = bike_day['season'].map(season_labels)

st.write(
    """
    # Menampilkan Jumlah Pengunjung paling ramai pada bulan apa ?
    """
)
# Penyewa berdasarkan bulan
rental_mnth = bike_day.groupby('mnth')['cnt'].mean()

plt.bar(rental_mnth.index, rental_mnth.values, color='#1f77b4')

plt.title('Rata - Rata penyewa perbulan')
plt.xlabel('bulan')
plt.ylabel('Rata - Rata penyewa')
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
           ['Jan', 'Febr', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])

plt.show()
st.pyplot() 
st.write(
    """
    # Menganalisa Jumlah Penyewa berdasarkan musim ?
    """
)
# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe
rental_season = bike_day.groupby('season_label')['cnt'].mean()

plt.bar(rental_season.index, rental_season.values, color='#1f77b4')

plt.title('Rata - Rata Penyewa permusim')
plt.xlabel('musim')
plt.ylabel('Rata - Rata Penyewa')

plt.show()

st.pyplot()  # Menggunakan st.pyplot() untuk menampilkan visualisasi di Streamlit

st.write(
    """
- Conclution pertanyaan 1 : Jumlah pengunjung paling ramai jatuh pada bulan Juni dan september
    * Pada bulan juni dan september adalah bulan yang paling disukai penyewa sepeda
- Conclution pertanyaan 2 : pengunjung paling sepi jatuh kepada musim spring dan paling ramai pengunjung berapa pada musim fall
    * Musim gugur(fall) merupakan musim peralihan dari musim panas ke musim dingin. Musim gugur adalah saat yang tepat pula untuk berjalan-jalan melihat daun berguguran yang warnanya sangat cantik. hal ini mungkin banyaknya penyewa sepeda yang ingin berjalan-jalan
    * Pada musim semi(spring), walaupun tidak lagi sedingin musim dingin, cuaca masih cukup dingin dan juga seringkali hujan. hal ini mungkin penyebab orang masih malas keluar
    """
)

st.set_option('deprecation.showPyplotGlobalUse', False)
