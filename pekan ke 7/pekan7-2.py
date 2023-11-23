# Input
nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")
pesan_menu = input("Pesan makanan atau minuman? (makanan/minuman): ")

# Menu makanan dan harga
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

# Menu minuman dan harga
menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

# Pilih menu berdasarkan pesan makanan atau minuman
if pesan_menu == "makanan":
    print("Menu Makanan:")
    for makanan, harga in menu_makanan.items():
        print(f"{makanan} - Harga: {harga} rupiah")
    pesanan = input("Masukkan pesanan makanan: ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
    harga_pesanan = menu_makanan.get(pesanan, 0) * jumlah_pesanan
elif pesan_menu == "minuman":
    print("Menu Minuman:")
    for minuman, harga in menu_minuman.items():
        print(f"{minuman} - Harga: {harga} rupiah")
    pesanan = input("Masukkan pesanan minuman: ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
    harga_pesanan = menu_minuman.get(pesanan, 0) * jumlah_pesanan
else:
    print("Pilihan tidak valid. Harap pilih 'makanan' atau 'minuman'.")

# Output
print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang di Pesan:", pesanan)
print("Jumlah Pesanan:", jumlah_pesanan)
print("Harga yang harus dibayarkan:", harga_pesanan, "rupiah")
