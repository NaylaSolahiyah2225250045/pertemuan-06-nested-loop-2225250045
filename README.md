# Pertemuan 06 Nested Loop Python
Nama: Nayla Solahiyah
NIM: 2225250045
Kelas: 3A

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan dalam program Python.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
Loop luar digunakan untuk menentukan baris dari 1 sampai n.
Loop dalam digunakan untuk menghitung hasil perkalian i * j pada setiap baris.
total_baris digunakan untuk menjumlahkan hasil perkalian pada setiap baris.
total_semua digunakan untuk menjumlahkan seluruh hasil perkalian.
count_genap digunakan untuk menghitung banyak hasil perkalian yang bernilai genap.

## Hasil Pengujian

| Input | Hasil yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| n = 1 | Total seluruh hasil = 1, banyak hasil genap = 0 | Total seluruh hasil = 1, banyak hasil genap = 0 | Lulus |
| n = 2 | Total seluruh hasil = 9, banyak hasil genap = 3 | Total seluruh hasil = 9, banyak hasil genap = 3 | Lulus |
| n = 3 | Total seluruh hasil = 36, banyak hasil genap = 5 | Total seluruh hasil = 36, banyak hasil genap = 5 | Lulus |
| n = 0 | Meminta input kembali | Meminta input kembali | Lulus |

## Analisis Efisiensi
Untuk input n, loop luar berjalan sebanyak n kali. Setiap satu kali loop luar, loop dalam juga berjalan sebanyak n kali. Jadi pernyataan `hasil = i * j` dieksekusi sebanyak n × n atau n² kali.

## Refleksi
Kesalahan yang dapat terjadi pada nested loop adalah menempatkan inisialisasi `total_baris` di luar loop luar. Jika dilakukan, jumlah dari baris sebelumnya akan ikut terbawa ke baris berikutnya. Cara memperbaikinya adalah mengatur `total_baris = 0` di awal setiap iterasi loop luar.

## Refleksi Teknis
1. `total_baris` direset di setiap iterasi loop luar karena variabel tersebut digunakan untuk menghitung jumlah pada satu baris saja.
2. `total_semua` tidak direset di setiap baris karena digunakan untuk menghitung jumlah seluruh hasil perkalian dari semua baris.
3. Untuk input n, pernyataan `hasil = i * j` dieksekusi sebanyak n² kali karena terdapat n iterasi pada loop luar dan n iterasi pada loop dalam.
4. `count_genap` dapat dibuktikan benar dengan menghitung setiap hasil yang memenuhi kondisi `hasil % 2 == 0`. Untuk n = 3, terdapat 5 hasil genap.
5. Bagian yang paling banyak melakukan operasi ketika n membesar adalah nested loop karena jumlah iterasinya bertambah menjadi n².