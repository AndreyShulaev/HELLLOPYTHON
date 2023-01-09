x = [2, 3, 5, 9, 3]
sum = 0
for i in range(0, len(x), 1):
    if i % 2 == 1:
        sum += x[i]       
print(f"{x} -> сумма элементов на нечётных позициях: {sum}")