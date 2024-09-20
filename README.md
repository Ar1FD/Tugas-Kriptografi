# Aplikasi Cipher Kriptografi

## Deskripsi
Aplikasi ini adalah GUI sederhana untuk melakukan enkripsi dan dekripsi teks menggunakan tiga jenis cipher klasik: Vigenere Cipher, Playfair Cipher, dan Hill Cipher. Aplikasi ini dibangun menggunakan `Tkinter` sebagai antarmuka grafis, dengan opsi input teks secara manual maupun melalui file.

## Fitur
- **Vigenere Cipher**: Enkripsi/dekripsi teks berdasarkan kunci yang diinput oleh pengguna.
- **Playfair Cipher**: Menggunakan matriks 5x5 berdasarkan kunci untuk mengenkripsi/dekripsi pasangan huruf.
- **Hill Cipher**: Menggunakan matriks kunci yang dimasukkan pengguna untuk mengenkripsi/dekripsi teks melalui operasi matriks.

## Persyaratan Sistem
- **Python 3.11** harus diinstal pada sistem.
- **Perpustakaan Python** yang dibutuhkan:
  - `Tkinter` (biasanya sudah tersedia pada instalasi standar Python)
  - `numpy` (untuk operasi matriks pada Hill Cipher)
