# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# my_f = open("Task41Sdz.txt", "w")
# k = int(input("Введите число:   "))
# lst = [random.randint(0,100) for i in range(k + 1)]
# print(lst)
# x = ""
# for i in range(k + 1):
#     if i < k:
#         x += str(lst[i]) + "*x^" + str(k-i)  +  " + " 
#     else:
#         x += str(lst[i])
# print(x)

# my_f.write(f'{x}  \n')
# my_f.close()
#===================================

#Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
#Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from itertools import *
from random import randint
import os
os.system("cls")


#k = randint(2, 7)  # случайным образом выбираем степень
k = int(input("Введите число:   "))
print('k = ', k)


def get_ratios(k):  # заполняем массив ratios случайными числами, чтобы первый элемент был не нулевой
    ratios = [randint(1, 9) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 9)
    return ratios


def get_polynomial(k, ratios):  # вычисляем полином, передаем степень и массив коэффициентов
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in zip_longest(
        ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

# перезаписываем результат в файл1, предыдущая запись обнуляется
with open('Task41Sdz_1.txt', 'w') as data:
    data.writelines(polynom1)
    data.writelines('\n')


# Второй многочлен для следующей задачи:

#k = randint(2, 5)

ratios = get_ratios(k)
print(ratios)
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('Task41Sdz_2.txt', 'w') as data:  # добавляем запись в файл
    data.write(polynom2)