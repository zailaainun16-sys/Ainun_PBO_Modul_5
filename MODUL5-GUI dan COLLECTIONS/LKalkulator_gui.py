import tkinter as tk
from tkinter import messagebox


class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu Celsius ke Fahrenheit")
        self.root.geometry("300x220")

        # Label input
        self.label_input = tk.Label(
            root,
            text="Masukkan Suhu (Celsius):",
            font=("Arial", 11)
        )
        self.label_input.pack(pady=10)

        # Entry Celsius
        self.entry_celsius = tk.Entry(root, width=25)
        self.entry_celsius.pack(pady=5)

        # Button konversi
        self.button_konversi = tk.Button(
            root,
            text="Konversi",
            command=self.konversi_suhu
        )
        self.button_konversi.pack(pady=10)

        # Label hasil
        self.label_hasil = tk.Label(
            root,
            text="Hasil: -",
            font=("Arial", 11)
        )
        self.label_hasil.pack(pady=10)

    def konversi_suhu(self):
        try:
            # Validasi input: harus berupa angka
            celsius = float(self.entry_celsius.get())
            fahrenheit = (celsius * 9 / 5) + 32
            self.label_hasil.config(
                text=f"Hasil: {fahrenheit:.2f} °F"
            )
        except ValueError:
            messagebox.showwarning(
                "Input Tidak Valid",
                "Masukkan suhu dalam bentuk angka!"
            )
            self.entry_celsius.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()
