c = int(input("Введите количество чисел: "))
while c <=0:
    print("Ошибка! Количество чисел должно быть больше нуля ")
    c = int(input("Введите количество чисел: "))
first = int(input("Введите первое число: "))
maximum = first
minimum = first
total = first
positive = 0
negative = 0
zeros = 0
if first > 0:
    positive += 1
elif first < 0:
    negative += 1
else:
    zeros += 1
for number in range(c - 1):
    number = int(input("Введите число: "))
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
    total += number
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zeros += 1
average = total / c
print(f"Максимальное число: {maximum}")
print(f"Минимальное число: {minimum}")
print(f"Сумма всех чисел: {total}")
print(f"Среднее значение: {average}")
print(f"Количество положительных чисел: {positive}")
print(f"Количество отрицательных чисел: {negative}")
print(f"Количество нулей: {zeros}")