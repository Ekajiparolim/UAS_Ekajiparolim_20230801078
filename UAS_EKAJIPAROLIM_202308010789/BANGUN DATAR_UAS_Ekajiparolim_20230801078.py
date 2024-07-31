import tkinter as tk
from tkinter import messagebox

# menghitung luas dan keliling
def hitung_luas_keliling():
    bangun_datar = var_bangun_datar.get()
    try:
        if bangun_datar == "Segi Empat":
            s = float(entri1.get())
            luas = s * s
            keliling = 4 * s
        elif bangun_datar == "Persegi Panjang":
            p = float(entri1.get())
            l = float(entri2.get())
            luas = p * l
            keliling = 2 * (p + l)
        elif bangun_datar == "Segitiga":
            a = float(entri1.get())
            t = float(entri2.get())
            s1 = float(entri3.get())
            s2 = float(entri4.get())
            luas = 0.5 * a * t
            keliling = s1 + s2 + a
        elif bangun_datar == "Lingkaran":
            r = float(entri1.get())
            luas = 3.14 * r * r
            keliling = 2 * 3.14159 * r
        hasil.set(f"Luas: {luas}\nKeliling: {keliling}")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka yang valid")

# kolom input 
def perbarui_kolom():
    bangun_datar = var_bangun_datar.get()
    if bangun_datar == "Segi Empat":
        label1.config(text="Sisi:")
        entri2.config(state="disabled")
        entri3.config(state="disabled")
        entri4.config(state="disabled")
    elif bangun_datar == "Persegi Panjang":
        label1.config(text="Panjang:")
        label2.config(text="Lebar:")
        entri2.config(state="normal")
        entri3.config(state="disabled")
        entri4.config(state="disabled")
    elif bangun_datar == "Segitiga":
        label1.config(text="Alas:")
        label2.config(text="Tinggi:")
        label3.config(text="Sisi 1:")
        label4.config(text="Sisi 2:")
        entri2.config(state="normal")
        entri3.config(state="normal")
        entri4.config(state="normal")
    elif bangun_datar == "Lingkaran":
        label1.config(text="Jari-jari:")
        entri2.config(state="disabled")
        entri3.config(state="disabled")
        entri4.config(state="disabled")

root = tk.Tk()
root.title("Kalkulator Bangun Datar")

var_bangun_datar = tk.StringVar(value="Segi Empat")
bangun_datar_options = ["Segi Empat", "Persegi Panjang", "Segitiga", "Lingkaran"]

# Widget
label_bangun_datar = tk.Label(root, text="Pilih Bangun Datar:")
label_bangun_datar.grid(row=0, column=0, pady=10)
bangun_datar_menu = tk.OptionMenu(root, var_bangun_datar, *bangun_datar_options, command=lambda _: perbarui_kolom())
bangun_datar_menu.grid(row=0, column=1, pady=10)

label1 = tk.Label(root, text="Sisi:")
label1.grid(row=1, column=0)
entri1 = tk.Entry(root)
entri1.grid(row=1, column=1)

label2 = tk.Label(root, text="Lebar:")
label2.grid(row=2, column=0)
entri2 = tk.Entry(root)
entri2.grid(row=2, column=1)

label3 = tk.Label(root, text="Sisi 1:")
label3.grid(row=3, column=0)
entri3 = tk.Entry(root)
entri3.grid(row=3, column=1)

label4 = tk.Label(root, text="Sisi 2:")
label4.grid(row=4, column=0)
entri4 = tk.Entry(root)
entri4.grid(row=4, column=1)

tombol_hitung = tk.Button(root, text="Hitung", command=hitung_luas_keliling)
tombol_hitung.grid(row=5, column=0, columnspan=2, pady=10)

hasil = tk.StringVar()
label_hasil = tk.Label(root, textvariable=hasil, relief="sunken", height=4, width=30)
label_hasil.grid(row=6, column=0, columnspan=2, pady=10)

perbarui_kolom()
root.mainloop()
