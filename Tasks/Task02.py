x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))

a = x * y * z
b = x + y + z

if a > 0:
    a = 0
elif a < 1:
    a = 1
if b > 0:
    b = 1
elif b < 1:
    b = 1

if a == b:
    print('Утверждение истинно')
elif a != b:
    print('Утверждение ложно')