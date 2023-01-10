# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5 
# 3*x² +10*x + 6 
# Вывод: 5*x² + 14*x + 11

from itertools import *
#from Task41Sdz import get_polynomial   # запускает весь скрипт на выполнение по оператору import, 
    # выход: if __name__ == "__main__":
    #           stuff only to run when not called via 'import' here
import os
os.system("cls")
print('+++++++++++++++++++++++++')

file1 = 'Task41Sdz_1.txt'
file2 = 'Task41Sdz_2.txt'

#exit()

def read_pol(file):  # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def convert_pol(pol):  # удалили "хвостик" и порезали" строку на массив , разделитель знак " + "
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
    pol = pol[::-1]
    return pol

def get_polynomial(k, ratios):  # вычисляем полином, передаем степень и массив коэффициентов
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in zip_longest(
        ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')

pol1 = read_pol(file1)
pol2 = read_pol(file2)
print('Исходные полиномы:')
print(pol1)
print(pol2)
print('_'*30)
print(convert_pol(pol1))
print(convert_pol(pol2))
pol1_coef = list(map(int, convert_pol(pol1)))
pol2_coef = list(map(int, convert_pol(pol2)))
print(pol1_coef)
print(pol2_coef)
print('_'*30)

sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
print(sum_coef)
sum_coef = sum_coef[::-1]
print(sum_coef)
sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
print('Итоговый результат сложения полиномов:\n', sum_pol)
with open('Task42Sdz.txt', 'w') as file_sum:
    file_sum.writelines(sum_pol)