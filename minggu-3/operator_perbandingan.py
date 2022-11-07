# print("======Program Cek Kelulusan======")
# nilai_uts = input("Masukkan Nilai UTS : ")
# nilai_uas = input("Masukkan Nilai UAS : ")
# nilai_akhir = (float(nilai_uts) + float(nilai_uas)) / 2
#
# if nilai_akhir < 90:
#     print("Nilai A", nilai_akhir)
# elif nilai_akhir > 80:
#     print('Nilai B', nilai_akhir)
# elif nilai_akhir <= 80:
#     print("Nilai C", nilai_akhir)
# else:
#     print("Nilai D", nilai_akhir)


input = 10
counter = 1

while input:
    if counter % 2 == 1:
        print(counter)

    counter += 2
    input -= 1

# for i in range(7):
#     if counter % 2 == 1:
#         print(counter)
#     counter += 2
