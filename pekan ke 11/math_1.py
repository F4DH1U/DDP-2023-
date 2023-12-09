import math

def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print("hasil tambah dari:",bil1,"+",bil2,"=",hasil)

def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print("hasil pengurangan dari:",bil1,"-",bil2,"=",hasil)

def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari:",bil1,"*",bil2,"=",hasil)

def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("hasil pembagian dari:",bil1,"/",bil2,"=",hasil)

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari:",bil1,"^",bil2,"=",hasil)

def faktorial(bil1):
    hasil = math.factorial(bil1)
    print("hasil faktorial dari:",bil1, "=",hasil)

def sin(bil1):
    hasil = math.sin(bil1)
    print("hasil Sin dari:",bil1,"=",hasil)

def log10(bil1):
    hasil = math.log10(bil1)
    print("hasil Log10 dari:",bil1,"=",hasil)

def hasil_bagi(bil1, bil2):
    hasil = bil1 // bil2
    print("hasil bagi dari:",bil1,"//",bil2,"=",hasil)

def sisa_bagi(bil1, bil2):
    hasil = bil1 % bil2
    print("hasil sisa bagi dari:",bil1,"%",bil2,"=",hasil)