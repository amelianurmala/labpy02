# labpy02

![Screenshot (58)](https://github.com/user-attachments/assets/96537b4c-8e3b-4b40-aa53-4bf1535673e3)


Berikut adalah penjelasan latihan 1:

### 1. Input Data
python
nama = input("Masukkan nama: ")
uts = input("Masukkan nilai UTS: ")
uas = input("Masukkan nilai UAS: ")
tugas = input("Masukkan nilai Tugas: ")

- *input()*: Fungsi ini digunakan untuk mengambil input dari pengguna. 
- *Variabel*:
  - nama: Menyimpan nama mahasiswa.
  - uts: Menyimpan nilai UTS (Ujian Tengah Semester).
  - uas: Menyimpan nilai UAS (Ujian Akhir Semester).
  - tugas: Menyimpan nilai tugas.

### 2. Menghitung Nilai Akhir
python
akhir = (int(tugas) * 0.2) + (int(uts) * 0.4) + (int(uas) * 0.4)

- *Menghitung Nilai Akhir*:
  - Nilai akhir dihitung berdasarkan bobot:
    - Tugas: 20% dari total (0.2).
    - UTS: 40% dari total (0.4).
    - UAS: 40% dari total (0.4).
- *int()*: Digunakan untuk mengonversi input dari tipe string menjadi integer agar dapat dilakukan perhitungan.

### 3. Menentukan Keterangan Lulus atau Tidak
python
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]

- *Indexing*: Menggunakan tuple untuk menentukan keterangan:
  - Jika akhir > 60.0, keterangan adalah "LULUS".
  - Jika tidak, keterangan adalah "TIDAK LULUS".

### 4. Menentukan Nilai Huruf
python
if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

- *Struktur Kontrol*: Menggunakan if, elif, dan else untuk menentukan nilai huruf berdasarkan nilai akhir:
  - A: jika akhir lebih dari 80.
  - B: jika akhir lebih dari 70.
  - C: jika akhir lebih dari 50.
  - D: jika akhir lebih dari 40.
  - E: jika tidak memenuhi syarat di atas.

### 5. Mencetak Hasil
python
print("\nNama :", nama)
print("Nilai UTS :", uts)
print("Nilai UAS :", uas)
print("Nilai Tugas :", tugas)
print("Nilai Akhir :", akhir)
print("\nNilai Huruf :", huruf)
print("Keterangan :", keterangan)

- *print()*: Menampilkan hasil kepada pengguna:
  - Nama mahasiswa, nilai UTS, UAS, tugas, nilai akhir, nilai huruf, dan keterangan kelulusan.

### Kesimpulan
Kode ini berfungsi untuk mengumpulkan nilai-nilai akademik dari pengguna, menghitung nilai akhir berdasarkan bobot yang telah ditentukan, serta memberikan keterangan mengenai kelulusan dan nilai huruf sesuai dengan kriteria yang ada.
