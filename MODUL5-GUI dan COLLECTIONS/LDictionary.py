# a. Membuat class Pelanggan
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email


# b. Membuat dictionary pelanggan (id sebagai key)
data_pelanggan = {
    "PL001": Pelanggan("PL001", "Hasan", "hasan@gmail.com"),
    "PL002": Pelanggan("PL002", "Ainun", "ainun@gmail.com"),
    "PL003": Pelanggan("PL003", "Sheila", "sheila@gmail.com")
}


# c. Fungsi untuk menambah pelanggan
def tambah_pelanggan(data_pelanggan, id_pelanggan, nama, email):
    if id_pelanggan in data_pelanggan:
        print("ID pelanggan sudah ada.")
    else:
        data_pelanggan[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)
        print("Pelanggan berhasil ditambahkan.")


# Fungsi untuk menghapus pelanggan
def hapus_pelanggan(data_pelanggan, id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("ID pelanggan tidak ditemukan.")


# Fungsi untuk mencari pelanggan
def cari_pelanggan(data_pelanggan, id_pelanggan):
    if id_pelanggan in data_pelanggan:
        return data_pelanggan[id_pelanggan]
    else:
        return None


# d. Menampilkan seluruh daftar pelanggan
print("=== Daftar Pelanggan ===")
if data_pelanggan:
    for id_pelanggan, pelanggan in data_pelanggan.items():
        print("-" * 30)
        print(f"ID    : {pelanggan.id_pelanggan}")
        print(f"Nama  : {pelanggan.nama}")
        print(f"Email : {pelanggan.email}")
else:
    print("Data pelanggan kosong.")


# Contoh penggunaan fungsi
print("\n=== Contoh Operasi ===")
tambah_pelanggan(data_pelanggan, "PL004", "Zaila", "zaila@gmail.com")

pelanggan_dicari = cari_pelanggan(data_pelanggan, "PL002")
if pelanggan_dicari:
    print(f"\nPelanggan ditemukan: {pelanggan_dicari.nama} - {pelanggan_dicari.email}")
else:
    print("\nPelanggan tidak ditemukan.")

hapus_pelanggan(data_pelanggan, "PL001")


# Menampilkan ulang daftar pelanggan setelah perubahan
print("\n=== Daftar Pelanggan Terbaru ===")
for id_pelanggan, pelanggan in data_pelanggan.items():
    print(f"{pelanggan.id_pelanggan} | {pelanggan.nama} | {pelanggan.email}")
