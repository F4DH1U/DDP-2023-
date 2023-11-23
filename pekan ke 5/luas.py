import math

def hitung_luas(pilihan):
    match pilihan:
        case 1:
            sisi = float(input("Masukkan panjang sisi: "))
            luas_persegi = sisi * sisi
            print(f"Luas persegi: {luas_persegi}")
        case 2:
            jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
            luas_lingkaran = math.pi * jari_jari ** 2
            print(f"Luas lingkaran: {luas_lingkaran}")
        case 3:
            alas = float(input("Masukkan panjang alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            luas_segitiga = 0.5 * alas * tinggi
            print(f"Luas segitiga: {luas_segitiga}")
        case _:
            print("Salah pilih angka")

pilihan = int(input('''selamat datang di aplikasi menghitung
masukan pilihan:
    1. untuk menghitung luas persegi
    2. untuk menghitung luas lingkaran
    3. untuk menghitung luas segitiga
      '''))
hitung_luas(pilihan)