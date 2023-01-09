# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 , 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#F−n = (−1)n+1 * Fn

# F−1 = 1,
# F−2 = -1,
# Fn = F(n+2)−F(n+1).

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

#fibo_nums = []
fibo_nums1 = get_fibonacci(n)
print(get_fibonacci(n))
#print(fibo_nums)
print(fibo_nums1.index(0))