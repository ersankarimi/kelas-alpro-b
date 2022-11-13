import sys

while True:
    print("""
===== Program Jumlahkan 2 Bilangan Integer=====
1. Masuk
2. Keluar""")

    pilihan = int(input("Masukkan Pilihan : "))

    if True:
        print("oke")
        print("iyakah")

    if pilihan == 1:
        print()
        print("Masukkan Bilangan")
        input_1 = int(input("Masukkan Bilangan 1 : "))
        input_2 = int(input("Masukkan Bilangan 2 : "))
        result = input_1 + input_2

        print(f"Hasil dari {input_1} + {input_2} = {result}")
    else:
        sys.exit()

    print()
