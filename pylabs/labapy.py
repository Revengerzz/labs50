#-*- coding: utf-8 -*-
import math
a = float(input('Введите а: '))
x = float(input('Введите х: '))
b = 0
i = 0
listG = []
listF = []
listY = []
listX = []
listA = []
count = int(input('Сколько считать? '))
m = float(input('Какой  шаг? '))
var = int(input('введи значение: '))

while count >= 0:
    if count == 0:
        con = str(input('продолжить счет:'))
        if con == 'да':
            count = int(input('Сколько считать? '))
            m = float(input('Какой  шаг? '))
        else:
            print('Все!')
    if var == 1:
        for i in range(count):
            if (18*(a**2)-11*a*x+x**2) == 0:
                print('Введены неверные данные')
            else:
                G = (56*(a**2)-488*a*x+320*(x**2))/(18*(a**2)-11*a*x+x**2)
                listG.append(G)
                listX.append(x)
                listA.append(a)
                x+=m
                a+=m
    elif var == 2:
        for i in range(count):
            z = math.sin(27*(a**2)+12*a*x-20*(x**2)-(math.pi/2))
            if math.isclose(z,b,abs_tol=0.000001):
    #if z != 0:
                print('Введены неверные данные')
            else:
                F = -1/(math.sin(27*(a**2)+12*a*x-20*(x**2)-(math.pi/2)))
                listF.append(F)
                listX.append(x)
                listA.append(a)
                a+=m
                x+=m
    elif var == 3:
        for i in range(count):
            if a==0.1 and x == 0.1:
                Y = math.asin(45*(a**2)+46*a*x+8*(x**2))
                listY.append(Y)
            else:
                print('Введены  неверные данные')
    else:
        print('Введены неверные данные')
    count -= 1

    if count == 0:
        vivod = str(input('Как выводить?(строка\табл) '))
        if vivod == 'строка':
            if var == 1:
                print(listG)
                print('Максимальный в G:')
                print(max(listG))
                print('Минимальный в G:')
                print(min(listG))
            elif var == 2:
                print(listF)
                print('Максимальный в F:')
                print(max(listF))
                print('Минимальный в F:')
                print(min(listF))
            else:
                print(listY)
                print('Максимальный в Y:')
                print(max(listY))
                print('Минимальный в Y:')
                print(min(listY))
        else:
            mda = 0
            if var == 1:
                for i in listG:
                    print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' G = ' + str(listG[mda]))
                    i += 1
                    mda += 1
            if var == 2:
                for i in listF:
                    print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' F = ' + str(listF[mda]))
                    i += 1
                    mda += 1
            if var == 3:
                for i in listY:
                    print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' Y = ' + str(listY[mda]))
                    i += 1
                    mda += 1
