#-*- coding: utf-8 -*-
import math
while True:
    try:
        a = float(input('Введите а: '))
        x = float(input('Введите х: '))
        count = int(input('Сколько считать? '))
        m = float(input('Какой  шаг? '))
        var = int(input('введи значение: '))
        break
    except:
        print('Попробй снова: ')
b = 0
i = 0
listF = []
listY = []
listX = []
listA = []
data = []
data2 = []
data3 = []
while count >= 0:
    if count == 0:
        while True:
            try:
                con = str(input('продолжить счет:'))
                break
            except:
                print('Попробуй снова: ')
        if con == 'да':
            while True:
                try:
                    count = int(input('Сколько считать? '))
                    m = float(input('Какой  шаг? '))
                    break
                except:
                    print(',Попробуйте снова: ')
        else:
            print('Все!')
    if var == 1:
        for i in range(count):
            if (18*(a**2)-11*a*x+x**2) == 0:
                print('Введены неверные данные')
            else:
                G = (56*(a**2)-488*a*x+320*(x**2))/(18*(a**2)-11*a*x+x**2)
                data.append((x, a, G))
		        listG.append(G)
#                listX.append(x)
#                listA.append(a)
#                kortezh1.append(a)
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
                data2.append((x, a, F))
                listF.append(F)
#                listX.append(x)
#                listA.append(a)
                a+=m
                x+=m
    elif var == 3:
        for i in range(count):
            if a==0.1 and x == 0.1:
                Y = math.asin(45*(a**2)+46*a*x+8*(x**2))
                listY.append(Y)
                data3.append((a, x, Y))
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
                for i in data:
                    print(i)
                   # print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' G = ' + str(listG[mda]))
                   # print('a = {} x = {} G = {}'.format(listA[mda], listX[mda], listG[mda]))
                   # i += 1
                   # mda += 1
            if var == 2:
                for i in data2:
                    print(i)
                   # print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' F = ' + str(listF[mda]))
                   # print('a = {} x = {} F = {}'.format(listA[mda], listX[mda], listF[mda]))
                   # i += 1
                   # mda += 1
            if var == 3:
                for i in data3:
                    print(i)
                   # print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' Y = ' + str(listY[mda]))
                   # print('a = {} x = {} Y = {}'.format(listA[mda], listX[mda], listY[mda]))
                   # i += 1
                   # mda += 1
MyFileData=open('test.txt','w')
for i in data:
    MyFileData.write(str(i) + '\n')
MyFileData.close()

MyFileData2=open('test2.txt','w')
for i in data2:
    MyFileData.write(str(i) + '\n')
MyFileData.close()

MyFileData3=open('test3.txt','w')
for i in data3:
    MyFileData.write(str(i) + '\n')
MyFileData.close()


file = open('test.txt','r')
numbers = [line for line in file.readlines()]
file.close()
for i in numbers:
    print(i)

file2 = open('test2.txt','r')
numbers2 = [line for line in file.readlines()]
file.close()
for i in numbers2:
    print(i)

file3 = open('test3.txt','r')
numbers3 = [line for line in file.readlines()]
file.close()
for i in numbers3:
    print(i)
