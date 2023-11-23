

```python
# Input
nama_kendaraan = input("Masukkan nama kendaraan (mobil/motor): ")
jenis_bensin = input("Masukkan jenis bensin (Pertalite/Pertamax/Pertamax Turbo): ")
kota_tujuan = input("Masukkan kota tujuan: ")
jarak_tempuh = float(input("Masukkan jarak tempuh kendaraan (KM): ")

# Harga bensin per liter
harga_pertalite = 10000
harga_pertamax = 14000
harga_pertamax_turbo = 17000

# Jarak tempuh untuk berbagai jenis bensin
jarak_tempuh_pertalite = 12
jarak_tempuh_pertamax = 13
jarak_tempuh_pertamax_turbo = 13.5

# Hitung pemakaian bensin
if jenis_bensin == "Pertalite":
    pemakaian_bensin = jarak_tempuh / jarak_tempuh_pertalite
    harga_per_liter = harga_pertalite
elif jenis_bensin == "Pertamax":
    pemakaian_bensin = jarak_tempuh / jarak_tempuh_pertamax
    harga_per_liter = harga_pertamax
elif jenis_bensin == "Pertamax Turbo":
    pemakaian_bensin = jarak_tempuh / jarak_tempuh_pertamax_turbo
    harga_per_liter = harga_pertamax_turbo

# Hitung total harga bensin
total_harga = pemakaian_bensin * harga_per_liter

# Output
print("Nama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota Tujuan:", kota_tujuan)
print("Pemakaian Bensin:", pemakaian_bensin, "liter")
print("Total Harga Bensin:", total_harga, "rupiah")
```

Anda dapat menjalankan program ini di lingkungan Python untuk menghitung total biaya perjalanan sesuai dengan jenis kendaraan, jenis bensin, dan jarak tempuh yang Anda masukkan.