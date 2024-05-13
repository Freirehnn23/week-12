def cek_elemen(tuple_pada_data):
    return all(elem == tuple_pada_data[0] for elem in tuple_pada_data)

input = eval(input("Masukkan Angka-Angka (pisahkan dengan koma): "))

if cek_elemen(input):
    print("True")
else:
    print("False")
