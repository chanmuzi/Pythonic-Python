from math import sqrt

temp = 1
flag = False
for i in range(5):
    num = int(input().rstrip())
    temp *= num
    if int(sqrt(temp))**2 == temp:
        flag = True
        break

if flag == True: print('found')
else: print('not found')