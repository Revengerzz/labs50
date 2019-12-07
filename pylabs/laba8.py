import random
import math
def coordinates(kol):
    data = []
    for i in range(kol):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        data.append((x,y))
    return(data)

def centre(dots):
    c = random.choice(dots)
    return(c)

def kollvo(tochki, centr, radius):
    count = 0
    for i in tochki:
        a = i
        if abs(a[0] - centr[0]) <= radius:
            if abs(a[1] - centr[1]) <= radius:
                count+=1
    return(count)

r = float(input('Введи радиус: '))
point = int(input('Введи кол-во точек: '))
points = coordinates(point)
print('Список точек: ', points)
mid = centre(points)
print()
print('Центр окружности: ', mid)
print()
ans = kollvo(points, mid, r)
if ans == 0:
    print('В данную область точки не входят')
else:
    print('Точек, входящих в окружность: ', ans)
