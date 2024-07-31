import tkinter as tk
from tkinter import messagebox

# menghitung total bayar
def hitung_total():
    try:
        lama_sewa = int(entry_lama_sewa.get())
        kode_kamar = entry_kode_kamar.get().upper()
        
        # harga sewa /malam berdasarkan kode
        if kode_kamar == 'M':
            harga_sewa = 650000
            nama_kamar = 'Melati'
        elif kode_kamar == 'S':
            harga_sewa = 550000
            nama_kamar = 'Sakura'
        elif kode_kamar == 'L':
            harga_sewa = 400000
            nama_kamar = 'Lily'
        elif kode_kamar == 'A':
            harga_sewa = 350000
            nama_kamar = 'Anggrek'
        else:
            messagebox.showerror("Error", "Kode kamar tidak valid!")
            return
        
        harga_kamar = harga_sewa * lama_sewa

        # diskon jika lebih dari 3 atau 5 hari
        if lama_sewa > 5:
            diskon = 0.10
        elif lama_sewa > 3:
            diskon = 0.05
        else:
            diskon = 0.0

        kamar_diskon = harga_kamar * (1 - diskon)
        
        # PPN
        ppn = 0.10 * kamar_diskon

        # total bayar
        total_bayar = kamar_diskon + ppn
        
        # Mendapatkan jumlah pembayaran dari input
        try:
            pembayaran = float(entry_pembayaran.get())
            if pembayaran < total_bayar:
                kembalian = 0.0
                messagebox.showwarning("Warning", "Jumlah pembayaran kurang dari total bayar!")
            else:
                kembalian = pembayaran - total_bayar
        except ValueError:
            pembayaran = 0.0
            kembalian = 0.0

        result_text.set(f"""
Bukti Pemesanan Kamar
HOTEL "SEJUK ASRI"
                        
Nama Petugas: {entry_nama_petugas.get()}            Nama Customer: {entry_nama_customer.get()}
                                             Tanggal Check-in: {entry_tanggal_checkin.get()}
                    ================================================                            
                                                        
Nama Kamar: {nama_kamar}
Harga Sewa per Malam: Rp {harga_sewa:,}
Lama Sewa: {lama_sewa} malam
harga kamar: Rp{harga_kamar}
PPN 10%: Rp {ppn:,}
Total Bayar: Rp {total_bayar:,}
Pembayaran: Rp {pembayaran:,}
Kembalian: Rp {kembalian:,}

        """)
        
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid! Pastikan lama sewa adalah angka.")

# Membuat window
window = tk.Tk()
window.title("Hotel SEJUK ASRI")

# Menentukan ukuran window
window_width = 700
window_height = 500

# Mendapatkan ukuran layar
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Menentukan posisi window di tengah layar
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)

window.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')

tk.Label(window, text="Nama Petugas:").grid(row=0, column=0, sticky='w')
entry_nama_petugas = tk.Entry(window)
entry_nama_petugas.grid(row=0, column=1)

tk.Label(window, text="Nama Customer:").grid(row=1, column=0, sticky='w')
entry_nama_customer = tk.Entry(window)
entry_nama_customer.grid(row=1, column=1)

tk.Label(window, text="Tanggal Check-in:").grid(row=2, column=0, sticky='w')
entry_tanggal_checkin = tk.Entry(window)
entry_tanggal_checkin.grid(row=2, column=1)

tk.Label(window, text="Pilih Kode Kamar M,S,L,A:").grid(row=3, column=0, sticky='w')
entry_kode_kamar = tk.Entry(window)
entry_kode_kamar.grid(row=3, column=1)

tk.Label(window, text="Lama Sewa per malam:").grid(row=4, column=0, sticky='w')
entry_lama_sewa = tk.Entry(window)
entry_lama_sewa.grid(row=4, column=1)

# Tombol untuk menghitung
btn_hitung = tk.Button(window, text="Hitung Total Bayar", command=hitung_total)
btn_hitung.grid(row=5, columnspan=2)

# menampilkan hasil
result_text = tk.StringVar()
tk.Label(window, textvariable=result_text).grid(row=6, columnspan=2)

#pembayaran
tk.Label(window, text="Input Pembayaran:").grid(row=7, column=0, sticky='w')
entry_pembayaran = tk.Entry(window)
entry_pembayaran.grid(row=7, column=1)

window.mainloop()
