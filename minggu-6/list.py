banyak_nilai = int(input("Masukkan Banyak Nilai : "))
nilai = []
result = 0

for i in range(banyak_nilai):
    input_nilai = input(f"Masukkan Nilai {i + 1} : ")

    nilai.append(float(input_nilai))

for index in range(len(nilai)):
    result += nilai[index]

print(f"Nilai rata-rata : {result / len(nilai)}")
