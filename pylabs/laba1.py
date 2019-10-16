from math import *
a = float(input())
x = float(input())
var = int(input('введи значение:'))
if var == 1:
    G = (56*(a**2)-488*a*x+320*(x**2))/(18*(a**2)-11*a*x+x**2)
    print(G)
elif var == 2:
    F = -1/(sin(27*(a**2)+12*a*x-20*(x**2)-(pi/2)))
    print(F)
elif var == 3:
    if a == 0.1 and x == 0.1:
        Y = asin(45*(a**2)+46*a*x+8*(x**2))
        print(Y)
    else:
        print('Введены  неверные данные')
else:
    print('error')
