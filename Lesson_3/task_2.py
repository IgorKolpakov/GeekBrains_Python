'''Задача: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5'''
from random import randint
input_set = [randint(1, 99) for i in range(int(input('Введите размер массива: ')))]
print(input_set)
num = int(input('Введите искомое число: '))
input_set = set(input_set)
dif = 0
if num > max(input_set):
    print(max(input_set))
elif num < min(input_set):
    print(min(input_set))
else:
    while True:
        if num - dif in input_set and num + dif in input_set and num - dif != num + dif:
            print(num - dif, num + dif)
            break
        elif num - dif in input_set:
            print(num - dif)
            break
        elif num + dif in input_set:
            print(num + dif)
            break
        else:
            dif += 1