# ЗАДАЧА1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным. Пример: - 6 -> да - 7 -> да - 1 -> нет
# d = int(input('Введите день недели в формате цифры, где 1 - это понедельник, 7 - воскресенье:'))
# if 1<=d<=5:
#     print('Это будний день')
# elif d==6 or d==7:
#     print('Это выходной день')
# else:
#     print('Введено некорректное число')

#ЗАДАЧА2
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:- x=34; y=-30 -> 4 # - x=2; y=4-> 1 # - x=-34; y=-30 -> 3
# x = int(input('Введите координату х: '))
# y = int(input('Введите коордитнату у:'))
# if x>0 and y>0:
#     print('Номер плоскости = 1')
# elif x<0 and y>0:
#     print('Номер плоскости = 2')
# elif x<0 and y<0:
#     print('Номер плоскости = 3')
# elif x>0 and y<0:
#     print('Номер плоскости = 4')
# else:
#     print('Некорректно задана координата')

#ЗАДАЧА4
# Напишите программу, которая по заданному номеру четверти показывает 
# диапазон возможных координат точек в этой четверти (x и y).
# qw = int(input('Введите номер плоскости координат: '))
# if qw == 1:
#     print('Диапазон координат в плоскости: x>0, y>0')
# elif qw == 2:
#     print('Диапазон координат в плоскости: x<0, y>0')
# elif qw == 3:
#     print('Диапазон координат в плоскости: x<0, y<0')
# elif qw == 4:
#     print('Диапазон координат в плоскости: x>0, y<0')
# else:
#     print('Такого номера плоскости не существует')

# ЗАДАЧА5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве. # Пример: # - A (3,6); B (2,1) -> 5,09

Xa = int(input('Введите координату Х для точки А: '))
Ya = int(input('Введите координату Y для точки А: '))
Xb = int(input('Введите координату Х для точки B: '))
Yb = int(input('Введите координату Y для точки B: '))
S = round(((Xb - Xa)**2 + (Yb - Ya)**2)**0.5, 2)
print(f'A ({Xa},{Xb})')
print(f'B ({Xb},{Yb})')
print('Расстояние между точками =', S)








    
    


    