# # # Function
# def sum(numbers):
#     result = 0
#
#     for number in numbers:
#         if "," in number or "." in number:
#             result += float(number)
#         else:
#             result += int(number)
#
#     return result
#
#
# many = int(input("Masukkan Banyak Angka : "))
# numbers = []
#
# for i in range(many):
#     number = input(f"Masukkan angka ke-{i + 1} : ")
#     numbers.append(number)
#
# print()
# print("Hasil dari penjumlahan adalah ", sum(numbers))


def factorial(batas):
    result = 1

    for i in range(batas):
        if batas - i != 0:
            result = result * (batas - i)

    return result


def factorial_recursive(number):
    if number == 1:
        return number
    else:
        return number * factorial_recursive(number - 1)


faktorial_5 = factorial_recursive(5)

print(faktorial_5)
