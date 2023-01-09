A_x = float(input('Введите координаты точки a по оси x:'))
A_y = float(input('Введите координаты точки a по оси y:'))
B_x = float(input('Введите координаты точки b по оси x:'))
B_y = float(input('Введите координаты точки b по оси y:'))

import math
distans = math.sqrt((A_x-B_x)**2+(A_y-B_y)**2)
print(f'Растояние между точкой A до точки B = {round(distans,2)}' )