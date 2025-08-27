# sreamlite-app
luas lingkaran
import math

def hitung_luas_lingkaran():
    print("=== Aplikasi Menghitung Luas Lingkaran ===")
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    
    luas = math.pi * (jari_jari ** 2)
    
    print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas:.2f}")

# Jalankan program
hitung_luas_lingkaran()


