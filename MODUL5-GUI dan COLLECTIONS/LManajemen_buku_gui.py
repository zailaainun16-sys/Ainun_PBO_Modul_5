import tkinter as tk
from tkinter import messagebox, ttk

#  Membuat class Tugas sebagai objek penyimpan data
class Tugas:
    def __init__(self, nama_tugas):
        self.nama_tugas = nama_tugas
        self.status = "Belum Selesai"

class AplikasiToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("500x450")

        # Koleksi list of objects untuk menyimpan data tugas
        self.daftar_tugas = []

        # --- UI Components ---
        self.label = tk.Label(root, text="Masukkan Tugas Baru:", font=("Arial", 10))
        self.label.pack(pady=5)

        self.entry_tugas = tk.Entry(root, width=40)
        self.entry_tugas.pack(pady=5)

        # Frame untuk Tombol Kontrol
        frame_aksi = tk.Frame(root)
        frame_aksi.pack(pady=10)

        self.btn_tambah = tk.Button(frame_aksi, text="Tambah", command=self.tambah_tugas, bg="lightgreen")
        self.btn_tambah.pack(side=tk.LEFT, padx=5)

        self.btn_selesai = tk.Button(frame_aksi, text="Tandai Selesai", command=self.tandai_selesai, bg="lightblue")
        self.btn_selesai.pack(side=tk.LEFT, padx=5)

        self.btn_edit = tk.Button(frame_aksi, text="Edit", command=self.edit_tugas, bg="yellow")
        self.btn_edit.pack(side=tk.LEFT, padx=5)

        self.btn_hapus = tk.Button(frame_aksi, text="Hapus", command=self.hapus_tugas, bg="red", fg="white")
        self.btn_hapus.pack(side=tk.LEFT, padx=5)

        # d. Menampilkan tugas dalam Treeview
        self.tree = ttk.Treeview(root, columns=("Tugas", "Status"), show="headings")
        self.tree.heading("Tugas", text="Nama Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.column("Status", width=100, anchor=tk.CENTER)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)

    # Implementasi Fitur Tambah
    def tambah_tugas(self):
        nama = self.entry_tugas.get()
        if nama:
            baru = Tugas(nama)
            self.daftar_tugas.append(baru)
            self.tree.insert("", tk.END, values=(baru.nama_tugas, baru.status))
            self.entry_tugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Isi tugas tidak boleh kosong!")

    # Implementasi Fitur Tandai Selesai
    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected)
            idx = self.tree.index(selected)
            
            # Update data di list of objects
            self.daftar_tugas[idx].status = "Selesai"
            # Update tampilan Treeview
            self.tree.item(selected, values=(self.daftar_tugas[idx].nama_tugas, "Selesai"))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin diselesaikan!")

    # Implementasi Fitur Hapus
    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            idx = self.tree.index(selected)
            self.daftar_tugas.pop(idx)
            self.tree.delete(selected)
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

    # Implementasi Fitur Edit
    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            teks_baru = self.entry_tugas.get()
            if teks_baru:
                idx = self.tree.index(selected)
                self.daftar_tugas[idx].nama_tugas = teks_baru
                self.tree.item(selected, values=(teks_baru, self.daftar_tugas[idx].status))
                self.entry_tugas.delete(0, tk.END)
            else:
                messagebox.showinfo("Info", "Ketik teks baru di kotak input untuk mengedit.")
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin diedit!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiToDo(root)
    root.mainloop()