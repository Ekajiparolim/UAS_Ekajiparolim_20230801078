import tkinter as tk
from tkinter import messagebox

# memasukkan data barang
def tambah_barang():
    nama = nama_entry.get()
    harga = harga_entry.get()
    stok = stok_entry.get()

    if not nama or not harga or not stok:
        messagebox.showwarning("Terjadi Kesalahan", "Semua kolom harus diisi!")
        return
    
    try:
        harga = float(harga)
        stok = int(stok)
    except ValueError:
        messagebox.showwarning("Kesalahan Input", "Harga harus berupa angka dan stok harus berupa bilangan bulat.")
        return
    
    barang[nama] = {'harga': harga, 'stok': stok}
    nama_entry.delete(0, tk.END)
    harga_entry.delete(0, tk.END)
    stok_entry.delete(0, tk.END)
    messagebox.showinfo("Sukses", "Barang ditambahkan!")

# menampilkan barang
def tampilkan_barang():
    teks_tampil = ""
    if not barang:
        teks_tampil = "Barang Tidak ada"
    else:
        for nama, detail in barang.items():
            teks_tampil += f"Nama: {nama}, Harga: {detail['harga']}, Stok: {detail['stok']}\n"
    messagebox.showinfo("Barang", teks_tampil)

# menghapus barang
def hapus_barang():
    nama = nama_entry.get()
    if nama in barang:
        del barang[nama]
        nama_entry.delete(0, tk.END)
        messagebox.showinfo("Sukses", "Barang berhasil dihapus!")
    else:
        messagebox.showwarning("Tidak Ditemukan", "Barang tidak ditemukan!")

# mencari barang
def cari_barang():
    nama = nama_entry.get()
    if nama in barang:
        detail = barang[nama]
        messagebox.showinfo("Barang Ditemukan", f"Nama: {nama}, Harga: {detail['harga']}, Stok: {detail['stok']}")
    else:
        messagebox.showwarning("Tidak Ditemukan", "Barang tidak ditemukan!")

# membeli barang
def beli_barang():
    nama = nama_entry.get()
    jumlah = stok_entry.get()

    if nama not in barang:
        messagebox.showwarning("Tidak Ditemukan", "Barang tidak ditemukan!")
        return
    
    if not jumlah:
        messagebox.showwarning("Kesalahan Input", "Jumlah harus diisi!")
        return
    
    try:
        jumlah = int(jumlah)
    except ValueError:
        messagebox.showwarning("Kesalahan Input", "Jumlah harus berupa bilangan bulat.")
        return
    
    if jumlah > barang[nama]['stok']:
        messagebox.showwarning("Tidak cukup", "Stok tidak mencukupi!")
        return
    
    barang[nama]['stok'] -= jumlah
    if barang[nama]['stok'] == 0:
        del barang[nama]
    stok_entry.delete(0, tk.END)
    messagebox.showinfo("Sukses", "Barang berhasil dibeli!")

root = tk.Tk()
root.title("Penginputan Barang")

barang = {}

tk.Label(root, text="Nama Barang").grid(row=0, column=0)
nama_entry = tk.Entry(root)
nama_entry.grid(row=0, column=1)

tk.Label(root, text="Harga").grid(row=1, column=0)
harga_entry = tk.Entry(root)
harga_entry.grid(row=1, column=1)

tk.Label(root, text="Stok").grid(row=2, column=0)
stok_entry = tk.Entry(root)
stok_entry.grid(row=2, column=1)

tk.Button(root, text="Tambah Barang", command=tambah_barang).grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Tampilkan Barang", command=tampilkan_barang).grid(row=4, column=0, columnspan=2)

tk.Button(root, text="Hapus Barang", command=hapus_barang).grid(row=5, column=0, columnspan=2)

tk.Button(root, text="Cari Barang", command=cari_barang).grid(row=6, column=0, columnspan=2)

tk.Button(root, text="Beli Barang", command=beli_barang).grid(row=7, column=0, columnspan=2)

root.mainloop()
