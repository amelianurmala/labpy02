# labpy02

![Screenshot (58)](https://github.com/user-attachments/assets/96537b4c-8e3b-4b40-aa53-4bf1535673e3)


### Berikut ini penjelasan kode latihan 1

1. *Shebang*: 

       #!/usr/bin/python3
   
   Ini adalah shebang yang menunjukkan bahwa skrip ini harus dijalankan menggunakan interpreter Python 3.
   
2. *Input Data*:
   
       nama = input("Masukkan nama: ")
       uts = input("Masukkan Nilai UTS: ")
       uas = input("Masukkan Nilai UAS: ")
       tugas = input("Masukkan Nilai Tugas: ")
   
   Program meminta pengguna untuk memasukkan nama dan nilai UTS, UAS, serta Tugas.

3. *Menghitung Nilai Akhir*:
   
       akhir = (int(tugas) * 0.2) + (int(uts) * 0.4) + (int(uas) * 0.4)
   
   - Nilai akhir dihitung berdasarkan bobot masing-masing komponen:
     
     - Tugas: 20%
       
     - UTS: 40%
       
     - UAS: 40%
       
   - Input nilai diubah menjadi integer menggunakan int() untuk melakukan perhitungan.

4. *Menentukan Keterangan Lulus/Gagal*:
   
       keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
   
   - Keterangan ditentukan dengan menggunakan tuple dan indexing. Jika akhir > 60.0, maka keterangan akan diambil dari indeks 1 (LULUS), jika tidak, dari indeks 0 (TIDAK LULUS).

5. *Menentukan Nilai Huruf*:
  
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
   
   - Berdasarkan nilai akhir, program menentukan huruf:
     - A: lebih dari 80
     - B: lebih dari 70
     - C: lebih dari 50
     - D: lebih dari 40
     - E: 40 atau kurang

  6. *Output Hasil*:
     
         print("\nNama :", nama)
         print("Nilai UTS :", uts)
         print("Nilai UAS :", uas)
         print("Nilai Tugas :", tugas)
         print("Nilai Akhir :", akhir)
         print("\nNilai Huruf :", huruf)
         print("Keterangan :", keterangan)
   
   - Hasil akhir, termasuk nama siswa, nilai UTS, UAS, Tugas, nilai akhir, nilai huruf, dan keterangan, dicetak ke layar.





![Screenshot (55)](https://github.com/user-attachments/assets/4866ad21-76e1-4417-a07d-4f0278b9feec)

### Berikut ini penjelasan kode latihan 2

1. *Input Gaji*:
 
       gaji = int(input("Masukkan gaji: "))
   
   Kode ini meminta pengguna untuk memasukkan gaji dan mengkonversinya menjadi tipe data integer.

2. *Status Keluarga*:
  
        berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T) ") == "Y"]
   
   Di sini, pengguna diminta untuk menjawab apakah sudah berkeluarga. Input diambil sebagai string, dan dibandingkan dengan "Y". Jika jawabannya "Y", maka berkeluarga akan bernilai         True; jika tidak, akan bernilai False.

3. *Kepemilikan Rumah*:

       punya_rumah = (False, True)[input("Punya rumah? (Y/T) ") == "Y"]
   
   Sama seperti status keluarga, pengguna ditanya apakah memiliki rumah. Jika jawabannya "Y", maka punya_rumah bernilai True; jika tidak, bernilai False.

4. *Pemeriksaan Gaji*:
   
       if gaji > 3000000:
   
   Program memeriksa apakah gaji yang dimasukkan lebih dari 3.000.000. Jika ya, maka akan menjalankan blok kode berikutnya.

5. *Output untuk Gaji di Atas UMR*:

       print("Gaji sudah di atas UMR")
   
   Jika gaji lebih dari 3.000.000, program mencetak pesan bahwa gaji sudah di atas UMR.

6. *Pemeriksaan Status Keluarga*:

       if berkeluarga:
         print("Wajib ikutan asuransi dan menabung untuk pensiun")
       else:
         print("Tidak perlu ikutan asuransi")
   
   Jika pengguna berkeluarga (berkeluarga bernilai True), program menyarankan untuk ikut asuransi dan menabung untuk pensiun. Jika tidak, program menyatakan bahwa tidak perlu ikut asuransi.

7. *Pemeriksaan Kepemilikan Rumah*:
 
       if punya_rumah:
         print("Wajib bayar pajak rumah")
       else:
         print("Tidak wajib bayar pajak rumah")
   
   Jika pengguna memiliki rumah (punya_rumah bernilai True), program menyatakan bahwa wajib membayar pajak rumah. Jika tidak, program menyatakan bahwa tidak wajib membayar pajak rumah.

8. *Output untuk Gaji di Bawah UMR*:
  
       else:
         print("Gaji belum UMR")
   
   Jika gaji kurang dari atau sama dengan 3.000.000, program mencetak pesan bahwa gaji belum mencapai UMR.





![Screenshot (59)](https://github.com/user-attachments/assets/e0620a02-6c84-40a3-886a-bea168d993a5)


### Berikut ini penjelasan kode latihan 3

1. *Input Bilangan*:
 
       a = int(input("Masukkan bilangan A: "))
       b = int(input("Masukkan bilangan B: "))
       c = int(input("Masukkan bilangan C: "))
   
   - Tiga bilangan (a, b, dan c) diambil dari input pengguna. Fungsi input() mengambil input sebagai string, dan int() mengkonversi string tersebut menjadi integer.

2. *Kondisi Pengecekan*:
   
       if a + b == c or b + c == a or c + a == b:
       
   - Menggunakan pernyataan if untuk memeriksa apakah jumlah dari dua bilangan sama dengan bilangan ketiga. Terdapat tiga kemungkinan:
     - Apakah a + b sama dengan c
     - Apakah b + c sama dengan a
     - Apakah c + a sama dengan b

3. *Output Hasil*:
 
       print("BENAR")
   
   - Jika salah satu kondisi di atas benar, program mencetak "BENAR".

   
         else:
             print("SALAH")
   
   - Jika tidak ada dari kondisi tersebut yang benar, program mencetak "SALAH".




  ![Screenshot (56)](https://github.com/user-attachments/assets/df750b9b-401c-4e2f-ba4c-cc1fe79d9e8b)


  ### Berikut ini penjelasan kode latihan 4


  1. *Inisialisasi Harga dan Diskon*:
  
         harga_tiket_reguler = 50000
         harga_tiket_vip = 100000
         diskon_member = 0.20
         
   - Dua variabel harga_tiket_reguler dan harga_tiket_vip menyimpan harga tiket untuk kategori reguler dan VIP. Variabel diskon_member menyimpan persentase diskon untuk anggota (20%).

2. *Meminta Input dari Pengguna*:
  
       tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
       status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()
   
   - Pengguna diminta untuk memasukkan tipe tiket yang diinginkan (reguler atau VIP) dan status keanggotaan (apakah memiliki kartu member atau tidak). Input dikonversi menjadi huruf kecil dengan .lower() untuk memudahkan perbandingan.

3. *Menghitung Harga Tiket Berdasarkan Tipe*:
   
       if tipe_tiket == "reguler":
           harga_tiket = harga_tiket_reguler
       elif tipe_tiket == "vip":
           harga_tiket = harga_tiket_vip
       else:
           print("Tipe tiket tidak valid.")
           exit()
   
   - Menggunakan struktur if-elif-else untuk menentukan harga tiket berdasarkan tipe yang dimasukkan:
     - Jika tipe tiket adalah "reguler", maka harga tiket diatur ke harga_tiket_reguler.
     - Jika tipe tiket adalah "vip", maka harga tiket diatur ke harga_tiket_vip.
     - Jika tipe tiket tidak valid, program mencetak pesan kesalahan dan keluar.

4. *Cek Status Member untuk Diskon*:
   
       if status_member == "ya":
           total_harga = harga_tiket * (1 - diskon_member)
       else:
           total_harga = harga_tiket
   
   - Memeriksa status keanggotaan:
     - Jika pengguna memiliki kartu member ("ya"), maka total harga dihitung dengan menerapkan diskon (20%).
     - Jika tidak, total harga sama dengan harga tiket yang telah ditentukan.

5. *Menampilkan Total Harga*:
   
       print(f"Total harga yang harus dibayar: Rp{int(total_harga)}")
   
   - Menampilkan total harga yang harus dibayar dengan format yang jelas, mengonversi nilai total harga menjadi integer untuk menghilangkan desimal.
  



   ![Screenshot (61)](https://github.com/user-attachments/assets/368d28b0-76e0-4f0e-bb8e-a368512007c8)

   ![Screenshot (62)](https://github.com/user-attachments/assets/6a899e0a-ab26-4f5d-9e68-6c81f80c7730)

### Berikut ini penjelasan kode latihan 5
   

1. *Input Angka dan Operator*:
  
       angka_pertama = float(input("Masukkan angka pertama: "))
       operator = input("Masukkan operator (+, -, *, /): ")
       angka_kedua = float(input("Masukkan angka kedua: "))
           
   - Pengguna diminta untuk memasukkan dua angka (angka_pertama dan angka_kedua) dan satu operator aritmatika (operator). Angka diambil sebagai tipe float untuk memungkinkan operasi desimal.

2. *Menentukan Operasi Aritmatika*:
   
       if operator == "+":
           hasil = angka_pertama + angka_kedua
       elif operator == "-":
           hasil = angka_pertama - angka_kedua
       elif operator == "*":
           hasil = angka_pertama * angka_kedua
       elif operator == "/":
           if angka_kedua != 0:
               hasil = angka_pertama / angka_kedua
           else:
               print("Error: Tidak bisa membagi dengan nol.")
               exit()
       else:
           print("Operator tidak valid.")
           exit()
       
   - Struktur if-elif-else digunakan untuk menentukan jenis operasi yang akan dilakukan berdasarkan nilai operator:
     - Jika operator adalah "+", maka dilakukan penjumlahan.
     - Jika operator adalah "-", maka dilakukan pengurangan.
     - Jika operator adalah "*", maka dilakukan perkalian.
     - Jika operator adalah "/", terdapat pengecekan tambahan untuk memastikan angka_kedua tidak nol sebelum melakukan pembagian. Jika nol, program mencetak pesan kesalahan dan keluar.
     - Jika operator tidak valid, program juga mencetak pesan kesalahan dan keluar.

3. *Menampilkan Hasil*:
  
       print(f"Hasil: {hasil}")
   
   - Setelah operasi selesai, hasil perhitungan ditampilkan kepada pengguna menggunakan format string.




