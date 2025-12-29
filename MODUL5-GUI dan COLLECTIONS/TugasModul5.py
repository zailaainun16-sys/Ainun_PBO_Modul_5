import tkinter as tk
from tkinter import messagebox, ttk

# Class Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = float(ipk)

    def info(self):
        return f"{self.nama} ({self.nim}) - {self.jurusan} - IPK: {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = float(ipk_baru)

class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("800x600")

        # Collections: Dictionary dengan NIM sebagai key
        self.data_mahasiswa = {}

        # --- GUI Layout ---
        # Frame Input
        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(pady=10, fill="x", padx=20)

        labels = ["NIM", "Nama", "Jurusan", "IPK"]
        self.entries = {}
        for i, text in enumerate(labels):
            tk.Label(frame_input, text=text + ":").grid(row=i//2, column=(i%2)*2, sticky="w", padx=5)
            entry = tk.Entry(frame_input)
            entry.grid(row=i//2, column=(i%2)*2+1, padx=5, pady=5)
            self.entries[text.lower()] = entry

        # Tombol CRUD
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Tambah/Update", command=self.simpan_mahasiswa, bg="lightgreen").pack(side="left", padx=5)
        tk.Button(frame_btn, text="Hapus", command=self.hapus_mahasiswa, bg="salmon").pack(side="left", padx=5)
        tk.Button(frame_btn, text="Cari", command=self.cari_mahasiswa).pack(side="left", padx=5)
        tk.Button(frame_btn, text="Export ke TXT", command=self.export_data).pack(side="left", padx=5)

        # Fitur Filter & Statistik
        frame_filter = tk.Frame(root)
        frame_filter.pack(pady=5)
        tk.Label(frame_filter, text="Filter Jurusan:").pack(side="left")
        self.ent_filter = tk.Entry(frame_filter)
        self.ent_filter.pack(side="left", padx=5)
        tk.Button(frame_filter, text="Filter", command=self.filter_jurusan).pack(side="left")
        tk.Button(frame_filter, text="Statistik", command=self.tampilkan_statistik, bg="lightblue").pack(side="left", padx=10)

        # Treeview
        self.tree = ttk.Treeview(root, columns=("NIM", "Nama", "Jurusan", "IPK"), show="headings")
        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

    # --- Logika Fungsi ---
    def validasi(self):
        try:
            float(self.entries['ipk'].get())
            if not (0 <= float(self.entries['ipk'].get()) <= 4.0):
                raise ValueError
            return True
        except:
            messagebox.showerror("Error", "IPK harus berupa angka 0.0 - 4.0")
            return False

    def simpan_mahasiswa(self):
        if self.validasi():
            nim = self.entries['nim'].get()
            mhs = Mahasiswa(nim, self.entries['nama'].get(), self.entries['jurusan'].get(), self.entries['ipk'].get())
            self.data_mahasiswa[nim] = mhs
            self.refresh_table()
            messagebox.showinfo("Sukses", "Data berhasil disimpan!")

    def hapus_mahasiswa(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected)['values'][0]
            del self.data_mahasiswa[str(nim)]
            self.refresh_table()
        else:
            messagebox.showwarning("Peringatan", "Pilih baris yang ingin dihapus")

    def refresh_table(self, dataset=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        display_data = dataset if dataset is not None else self.data_mahasiswa.values()
        for mhs in display_data:
            self.tree.insert("", "end", values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def cari_mahasiswa(self):
        key = self.entries['nim'].get().lower() or self.entries['nama'].get().lower()
        hasil = [m for m in self.data_mahasiswa.values() if key in m.nim.lower() or key in m.nama.lower()]
        self.refresh_table(hasil)

    def filter_jurusan(self):
        jur = self.ent_filter.get().lower()
        hasil = [m for m in self.data_mahasiswa.values() if jur in m.jurusan.lower()]
        self.refresh_table(hasil)

    # Fitur Tambahan: Statistik
    def tampilkan_statistik(self):
        if not self.data_mahasiswa: return
        ipks = [m.ipk for m in self.data_mahasiswa.values()]
        rata = sum(ipks) / len(ipks)
        tertinggi = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        
        info = f"Rata-rata IPK: {rata:.2f}\nIPK Tertinggi: {tertinggi.nama} ({tertinggi.ipk})"
        messagebox.showinfo("Statistik Mahasiswa", info)

    # Export Data
    def export_data(self):
        with open("data_mahasiswa.txt", "w") as f:
            for m in self.data_mahasiswa.values():
                f.write(f"{m.nim},{m.nama},{m.jurusan},{m.ipk}\n")
        messagebox.showinfo("Sukses", "Data diexport ke data_mahasiswa.txt")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()