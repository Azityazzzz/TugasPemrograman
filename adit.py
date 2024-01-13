print("===============TOKO JONNNN==========")
pembeli = input("Nama pembeli : ")
# Stok barang
stok_barang = [
    {"nama": "Indomie", "harga": 3000, "jumlah": 100},
    {"nama": "Teh Pucuk", "harga": 4000, "jumlah": 70},
    {"nama": "Coca-Cola", "harga": 6000, "jumlah": 50},
]

# Function untuk menampilkan stok barang
def tampilkan_stok():
    print("--------------------------")
    print("       Daftar Barang   ")
    print("          Teh Pucuk         ")
    print("           Indomie          ")
    print("          Coca-Cola         ")
    print("---------------------------")
    for item in stok_barang:
        print(f"Nama: {item['nama']}, Harga: {item['harga']}, Jumlah: {item['jumlah']}")
    print("-------------------------")

# Function untuk menginput nama barang dan jumlah yang dibeli
def input_barang():
    nama_barang = input("Masukkan nama barang: ")
    jumlah_beli = int(input("Masukkan jumlah pembelian: "))
    return nama_barang, jumlah_beli

# Function untuk melakukan pembelian
def pembelian():
    tampilkan_stok()
    nama_barang, jumlah_beli = input_barang()
    for item in stok_barang:
        if item["nama"] == nama_barang:
            if item["jumlah"] >= jumlah_beli:
                total_harga = item["harga"] * jumlah_beli
                print(f"Total harga pembelian: {total_harga}")
                print("Terimakasih")
                print("=============================")
                item["jumlah"] -= jumlah_beli
                return
            else:
                print("Stok barang tidak mencukupi!")
                return
    print("Barang tidak ditemukan!")

# Function untuk menjalankan program
def main():
    while True:
        print("\n\n=====================")
        print("       Kasir      ")
        print("=====================")
        print("1. Lihat Stok Barang")
        print("2. Melakukan Pembelian")
        print("3. Keluar")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            tampilkan_stok()
        elif pilihan == 2:
            pembelian()
        elif pilihan == 3:
            break
        else:
            print("Pilihan tidak valid silahkan pilih kembali!")

if __name__ == "__main__":
    main()
    print("Silakan melakukan pembayaran ")
    print("Terimakasih")
    print("=============================")