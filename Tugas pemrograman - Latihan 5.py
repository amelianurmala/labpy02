# Meminta input angka pertama, operator, dan angka kedua dari pengguna
angka_pertama = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka_kedua = float(input("Masukkan angka kedua: "))

# Menggunakan if elif else untuk menentukan operasi aritmatika
if operator == "+":
    hasil = angka_pertama + angka_kedua
elif operator == "-":
    hasil = angka_pertama - angka_kedua
elif operator == "*":
    hasil = angka_pertama * angka_kedua
elif operator == "/":
    # Mengecek apakah angka kedua nol untuk menghindari pembagian dengan nol
    if angka_kedua != 0:
        hasil = angka_pertama / angka_kedua
    else:
        print("Error: Tidak bisa membagi dengan nol.")
        exit()
else:
    print("Operator tidak valid.")
    exit()

# Menampilkan hasil perhitungan
print(f"Hasil: {hasil}")
