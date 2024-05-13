nama_file = input("Enter a file name: ")
file_handle = open(nama_file)

jam_distribusi = dict()

for baris in file_handle:
    if baris.startswith('From '):
        kata = baris.split()
        jam = kata[5].split(':')[0]
        jam_distribusi[jam] = jam_distribusi.get(jam, 0) + 1

for jam, hitung in sorted(jam_distribusi.items()):
    print(jam, hitung)
