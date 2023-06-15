# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a1 = int(input("Введите первый элемент число: "))
d = int(input("Введите разность элементов: "))
n = int(input("Введите кол-во элементов: "))
for i in range(n):
    print(a1 + (i * d), end=' ')


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [3, 40, 0, 44, 4, -2, 2, 1, 1, 2, 2, 10, 11, 12, 14, 13, 33, 31, 14, 5]
list_2 = []
one_num = 10
second_num = 12

for i in range(len(list_1)):
    if one_num <= list_1[i] <= second_num:
        print(i, end=' ')