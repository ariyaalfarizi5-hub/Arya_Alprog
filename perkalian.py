#Program Tabel Perkalian
#======VERIFIKASI NAMA=====

NAMA_BENAR = "arya"
while True:
    nama = input("Masukkan nama anda : ").lower().strip(
        if nama == NAMA_BENAR:
        
        print(f"\nSelamat datang, {nama. title()}!")
        print("Lanjut ke program selanjutnya...\n")
        break  # Lanjut ke program selanjutnya
    else
    print("silahkan coba logi\n")

#TABEL PERKALIAN

print("=" * 30)
print("PROGRAM TABEL PERKALIAN")
print("=" * 30)

# minta user masukkan angka
angkan= int(input("\nMasukkan angka: "))

print()  # Baris Kosong

# Tampilkan tabel perkalian 1 sampai 10
for i in range(1, 11):
    hasil = angka * 1
    print(f"{angka} x {i} = {hasil}")

print("\nProgram selesai!")
