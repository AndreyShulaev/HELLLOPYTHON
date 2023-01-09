#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
list1 = []
# Min=list[0] % 1
# Max=list[0] % 1
for i in range(len(list)):
    if list[i] % 1 != 0:
        list1.append(list[i])
        # if list[i] % 1 > Max:
        #     Max=list[i] % 1
        # if list[i] % 1 < Min:
        #     Min=list[i] % 1        
x2 = [round(list1[i] % 1, 2) for i in range(len(list1))]
print(f"{x2} => {max(x2) - min(x2)}")
#print(f"{Max} - {Min} = {round(Max - Min,2)}")
