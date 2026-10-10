# BAB 11 - Mini Project Rekap Nilai per Kelas

import csv

# Membaca data siswa
data = []

with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# Mengelompokkan nilai berdasarkan kelas
rekap = {}

for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

# Menampilkan rekap nilai
print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")

for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")