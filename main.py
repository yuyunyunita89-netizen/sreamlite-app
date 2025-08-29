import math
import streamlit as st

# Judul aplikasi
st.title("🟢 Aplikasi Menghitung Luas Lingkaran")

# Input jari-jari dari web (bukan console)
jari_jari = st.number_input(
    "Masukkan jari-jari lingkaran:",
    min_value=0.0,
    step=0.1,
    format="%.2f"
)

# Tombol untuk menghitung
if st.button("Hitung Luas"):
    if jari_jari > 0:
        luas = math.pi * (jari_jari ** 2)
        st.success(f"Luas lingkaran dengan jari-jari {jari_jari:.2f} adalah: {luas:.2f}")
    else:
        st.warning("⚠️ Silakan masukkan jari-jari lebih dari 0")
