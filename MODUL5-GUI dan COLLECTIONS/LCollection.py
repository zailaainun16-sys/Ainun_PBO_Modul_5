# Membuat class Buku
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun


# Membuat list berisi 5 objek buku
daftar_buku = [
    Buku("Pemrograman Python", "Hasan", 2020),
    Buku("Basis Data", "Ainun", 2019),
    Buku("Struktur Data", "Herdi", 2021),
    Buku("Algoritma dan Pemrograman", "Zaila", 2018),
    Buku("Pemrograman Berorientasi Objek", "Sheila", 2022)
]


# Fungsi untuk mencari buku berdasarkan penulis
def cari_buku_berdasarkan_penulis(daftar_buku, nama_penulis):
    hasil = []
    for buku in daftar_buku:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil


# Menampilkan hasil pencarian
penulis_dicari = "Hasan"
hasil_pencarian = cari_buku_berdasarkan_penulis(daftar_buku, penulis_dicari)

print("=== Hasil Pencarian Buku ===")
print(f"Penulis: {penulis_dicari}")

if hasil_pencarian:
    for buku in hasil_pencarian:
        print("-" * 30)
        print(f"Judul   : {buku.judul}")
        print(f"Penulis : {buku.penulis}")
        print(f"Tahun   : {buku.tahun}")
else:
    print("Buku tidak ditemukan.")
