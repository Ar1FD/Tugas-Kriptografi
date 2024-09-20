# Aplikasi Cipher Kriptografi

## Deskripsi
Aplikasi ini adalah GUI sederhana untuk melakukan enkripsi dan dekripsi teks menggunakan tiga jenis cipher klasik: Vigenere Cipher, Playfair Cipher, dan Hill Cipher. Aplikasi ini dibangun menggunakan `Tkinter` sebagai antarmuka grafis, dengan opsi input teks secara manual maupun melalui file. Aplikasi ini dibuat sebagai tanda bukti penyelesaian tugas kriptografi yang diampu oleh Pak Alamsyah pada mata kuliah kriptografi.

## Fitur
- **Vigenere Cipher**: Enkripsi/dekripsi teks berdasarkan kunci yang diinput oleh pengguna.
- **Playfair Cipher**: Menggunakan matriks 5x5 berdasarkan kunci untuk mengenkripsi/dekripsi pasangan huruf.
- **Hill Cipher**: Menggunakan matriks kunci yang dimasukkan pengguna untuk mengenkripsi/dekripsi teks melalui operasi matriks.

## Persyaratan Sistem
- **Python 3.11** harus diinstal pada sistem.
- **Perpustakaan Python** yang dibutuhkan:
  - `Tkinter` (biasanya sudah tersedia pada instalasi standar Python)
  - `numpy` (untuk operasi matriks pada Hill Cipher)

## Cara Menjalankan Program

### 1. Clone Repository
Clone repository dari GitHub ke komputer lokal Anda.
```bash
https://github.com/Ar1FD/Tugas-Kriptografi.git
```

## 2. Instalasi Perpustakaan yang Dibutuhkan
Pastikan `numpy` telah diinstal. Jika belum, install dengan menjalankan perintah berikut di terminal:
```bash
pip install numpy
```

## 3. Menjalankan Program
Untuk menjalankan aplikasi, navigasikan ke direktori tempat program disimpan dan jalankan perintah berikut:
```bash
python Kriptografi.py
```

## 4. Cara Menggunakan Aplikasi
- Pilih salah satu cipher: **Vigenere**, **Playfair**, atau **Hill**.
- Masukkan pesan yang ingin dienkripsi atau didekripsi melalui teks atau dengan mengunggah file `.txt`.
- Masukkan kunci dengan panjang minimal 12 karakter.
- Untuk **Hill Cipher**, ketika memilih opsi enkripsi atau dekripsi, Anda akan diminta untuk memasukkan matriks kunci dalam format matriks (misal: `[[2, 3], [1, 6]]`).
- Klik tombol **Enkripsi** atau **Dekripsi** untuk mendapatkan hasilnya.

## Catatan
- Kunci untuk setiap cipher harus minimal 12 karakter.
- Untuk **Hill Cipher**, pastikan matriks kunci yang dimasukkan adalah matriks persegi yang valid.
- Hasil enkripsi atau dekripsi akan ditampilkan pada area teks di bagian bawah aplikasi.

