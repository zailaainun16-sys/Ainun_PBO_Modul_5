import tkinter as tk
from tkinter import messagebox

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi GUI Sederhana")
root.geometry("300x200")

# Fungsi menampilkan isi Entry ke messagebox
def tampilkan_pesan():
    teks = entry.get()
    if teks:
        messagebox.showinfo("Pesan", f"Isi Entry: {teks}")
    else:
        messagebox.showwarning("Peringatan", "Entry masih kosong!")

# Fungsi menghapus isi Entry
def hapus_entry():
    entry.delete(0, tk.END)

# Label
label = tk.Label(root, text="Masukkan Teks:")
label.pack(pady=10)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button tampilkan
button_tampil = tk.Button(root, text="Tampilkan", command=tampilkan_pesan)
button_tampil.pack(pady=5)

# Button hapus
button_hapus = tk.Button(root, text="Hapus", command=hapus_entry)
button_hapus.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
