list1 = [2, 3, 4, 5, 3, 5, 2]

import math 
size = math.ceil(len(list1)/2)
#print(size)
list2 = []
for i in range(size):
    list2.append(list1[i]*list1[-i-1])
print(list1)
print(list2)