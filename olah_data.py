# BAB 11 - Filter, Hitung & Cari Nilai Tertinggi

import csv

# Membaca data dari file CSV
data = []

with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# Menghitung rata-rata nilai
nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)

print(f"Rata-rata: {rata:.1f}")

# Mencari siswa yang lulus
lulus = [d["nama"] for d in data
         if d["nilai"] >= 75]

print("Lulus:", lulus)

# Mencari nilai tertinggi
top = max(data, key=lambda d: d["nilai"])

print("Tertinggi:", top["nama"])