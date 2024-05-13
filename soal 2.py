nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")
alamat = input("Masukkan Alamat: ")

nim_ke_tuple = tuple(nim)
nama_ke_tuple = tuple(nama.split())
alamat_ke_tuple = tuple(alamat.split(","))

nim_full = ''.join(nim_ke_tuple)
nama_full = ' '.join(nama_ke_tuple)
alamat_full = ' '.join(alamat_ke_tuple)

nim_fix= nim_ke_tuple
nama_fix = (nama_ke_tuple[::1])
nama_terbalik = tuple(reversed(nama_ke_tuple [::-1]))

print(f"NIM : {nim_full}")
print(f"NAMA : {nama_full.title()}")
print(f"ALAMAT : {alamat_full.strip()}")
print(f"NIM: {nim_fix}")
print(f"NAMA DEPAN : {nama_fix[0]}")
print(f"NAMA TERBALIK : {nama_terbalik[::-1]}")