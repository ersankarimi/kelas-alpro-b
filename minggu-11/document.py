import os
import sys


def masuk(username, password):
    if not cek_file():
        file = open("data.txt", "x")
        file.close()

    file = open("data.txt", "r")
    file_data = file.read().split("\n")

    # Lakukan perulangan sebanyak panjang data dari file_data variabel
    for i in range(len(file_data)):
        # Buat pengecekan terhadap data `i`
        #  apakah sama dengan username,password
        if file_data[i] != f"{username},{password}":
            if i == len(file_data) - 1:
                print("\n====Data Tidak Ditemukan...\nSilahkan Daftar Dulu====\n")
        else:
            print("\n===Berhasil Masuk ke Sistem===\n")
            return

    file.close()
    print()


def cek_file():
    if os.path.exists("data.txt"):
        return True
    else:
        return False


def daftar(username, password):
    # Masukkan data username dan password ke dalam data.txt
    # Format data disimpan itu username,password
    # Contoh username = "saya", password ="kamu", maka data yang dimasukkan aku,kamu
    # Untuk lebih jelasnya liat contoh data pada file data.txt
    pass


def lupa_password(username):
    # Cari data yang sesuai dengan argumen username pada parameter
    # Jika di temukan data dengan username tersebut maka buatlah inputan password baru
    # Lalu timpa semua data konten yang ada di data.txt dengan data yang sebelumnya ada
    # Jangan lupa masukkan juga data yang sudah diganti passwordnya

    # Jika data tidak ditemukanm maka cetak ke konsol terminal "=====Username Tidak Ditemukan===="
    # Lalu kembali ke menu awal lagi
    pass


def baca_data():
    # Iterasi semua data dalam data.txt
    # Dan cetak ke konsol terminal dengan format seperti dibawah ini

    # Contoh data dalam data.txt
    # admin,root1234
    # admin1,admin123

    # Maka saat dicetak akan ditampilkan seperti dibawah ini

    # Data 1
    # Username : admin
    # Password : root1234

    # Data 2
    # (mengikuti seperti contoh diatas)
    pass


def keluar():
    sys.exit()


while True:
    print("""Pilih Menu [1-3]
1. Masuk
2. Daftar
3. Lupa Password
4. Baca Data
5. Keluar""")
    input_pilihan = int(input("Masukkan pilihan menu [1-3] : "))

    if input_pilihan > 5:
        print("\n=====Masukkan Pilihan yang Benar!=====\n")
        continue

    if input_pilihan == 1:
        print("\n=== Masuk ke Sistem ===\n")

        username = input("Masukkan username : ")
        password = input("Masukkan password : ")

        masuk(username, password)
