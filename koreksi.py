print("====Program Pemangkatan====")


def pemangkatan(nilai, pangkat):
    if pangkat == 0:
        return 1
    else:
        return nilai * pemangkatan(nilai, pangkat - 1)


nilai = int(input("Masukkan Nilai : "))
pangkat = int(input("Masukkan Pangkat : "))
print()

print(f"Nilai Perpangkatan dari : ({nilai}, {pangkat})")
print(f"Hasil Perpangkatan : {pemangkatan(nilai, pangkat)}")
