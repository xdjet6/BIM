numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
none_nomer = numbers.index(None)
summa = 0
z = 0
for x in numbers:
    if x is not None:
        summa = summa + x
        z = z + 1
srednee = summa/z
numbers[none_nomer] = srednee
print("Измененный список:", numbers)