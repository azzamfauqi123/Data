# Analisis Data Bikeshare dan Visualisasi Data dengan Dashboard Interaktif menggunakan streamlit
http://capitalbikeshare.com/system-data

## Analisi dFata menggunakan colab google

### Rumusan Masalah

1.  bagaimana pengaruh pola-pola jumlah pengguna Bikeshare dapat dipengaruhi musim, cuaca, dan faktor pendukung seperti suhu, kelembaban, dan kecepatan angin?

2.   Apakah korelasi antara bulan dan musim dapat berimplikasi terhadap jumlah pengguna Bikeshare?


### Kesimpulan
Berdasarkan hasil pengamatan kondisi cuaca dan musim, serta pola peminjaman sepeda di setiap musim, kita dapat membuat beberapa hubungan yang mungkin:



*   Musim dan Jumlah Peminjaman: Terdapat korelasi antara musim dengan jumlah peminjaman sepeda. Misalnya, pada musim panas yang memiliki suhu yang nyaman, jumlah peminjaman sepeda mungkin meningkat karena kondisi cuaca yang mendukung aktivitas di luar ruangan. Sebaliknya, pada musim hujan yang memiliki suhu yang lebih rendah dan kemungkinan hujan lebih tinggi, jumlah peminjaman sepeda mungkin menurun.
*  Kondisi Cuaca dan Jumlah Peminjaman: Cuaca juga dapat mempengaruhi jumlah peminjaman sepeda. Cuaca yang cerah dan nyaman cenderung meningkatkan minat orang untuk bersepeda, sementara cuaca buruk seperti hujan berat atau kabut tebal mungkin mengurangi minat untuk bersepeda. Oleh karena itu, kondisi cuaca yang baik biasanya akan menyebabkan peningkatan jumlah peminjaman sepeda.

*   Rentang Suhu dan Kondisi Cuaca dengan Jumlah Peminjaman: Rentang suhu dan kondisi cuaca tertentu dalam setiap musim dapat memiliki dampak yang berbeda pada jumlah peminjaman sepeda. Misalnya, pada musim gugur dengan suhu yang nyaman antara 25-30 derajat Celsius, jumlah peminjaman sepeda mungkin meningkat karena kondisi cuaca yang menyenangkan untuk bersepeda.
*   Rentang Suhu dan Kondisi Cuaca dengan Jumlah Peminjaman: Rentang suhu dan kondisi cuaca tertentu dalam setiap musim dapat memiliki dampak yang berbeda pada jumlah peminjaman sepeda. Misalnya, pada musim gugur dengan suhu yang nyaman antara 25-30 derajat Celsius, jumlah peminjaman sepeda mungkin meningkat karena kondisi cuaca yang menyenangkan untuk bersepeda.


*   Distribusi Cuaca dalam Setiap Bulan dengan Jumlah Peminjaman: Distribusi cuaca dalam setiap bulan juga dapat mempengaruhi jumlah peminjaman sepeda. Cuaca yang cerah dan stabil sepanjang tahun mungkin meningkatkan konsistensi peminjaman sepeda, sementara cuaca ekstrim seperti hujan berat yang hanya terjadi pada bulan tertentu mungkin mengakibatkan penurunan tajam dalam jumlah peminjaman pada bulan tersebut.
*   Dengan memahami pola musim, kondisi cuaca, dan preferensi pengguna terhadap kondisi cuaca, operator penyewaan sepeda dapat mengoptimalkan layanan mereka dengan menyesuaikan strategi pemasaran, penjadwalan inventaris, dan pengelolaan operasional.













## Dashboard Interaktif Menggunakan Streamlit



Dashboard menunjukkan jumlah total perjalanan sepanjang tahun dan musim. Hal ini juga menunjukkan perbedaan penggunaan layanan bikesharing antara pengendara biasa dan pengendara terdaftar, berdasarkan jam dan hari dalam seminggu.



### Run Streamlit on Local

#### Install Dependencies

To install all the required libraries, open your terminal/command prompt/conda prompt, navigate to this project folder, and run the following command:

```bash
pip install -r requirements.txt
```

#### Run Dashboard
```bash
cd dashboard
streamlit run dashboard.py
```


