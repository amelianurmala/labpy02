# Harga tiket bioskop
harga_tiket_reguler = 50000
harga_tiket_vip = 100000
diskon_member = 0.20

# Meminta input dari user
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# Menghitung harga tiket berdasarkan tipe
if tipe_tiket == "reguler":
    harga_tiket = harga_tiket_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_tiket_vip
else:
    print("Tipe tiket tidak valid.")
    exit()

# Cek status member untuk diskon
if status_member == "ya":
    total_harga = harga_tiket * (1 - diskon_member)
else:
    total_harga = harga_tiket

# Menampilkan total harga yang harus dibayar
print(f"Total harga yang harus dibayar: Rp{int(total_harga)}")