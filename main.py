# 1

import random

print('Задание 1, генерация списка чискл заданной длинны')
print(random.sample(range(10, 100), 10))
print('-------------------------\n')
# 2
import random
from functools import reduce

print('Задание 2, Максимум числ из списка')
list1 = random.sample(range(10, 100), 10)
print(list1)
print(reduce(max, list1))
print('-------------------------\n')
# 3
import random

print('Задание 3, Суммирование всех чисел в списке')
list1 = random.sample(range(0, 10), 10)
print(list1)
print(sum(list1))
print('-------------------------\n')

# 4

from functools import reduce
from operator import mul

print('Задание 4, умножение всех чисел в списке')
list1 = random.sample(range(2, 12), 10)
print(list1)
print(reduce(mul, list1))
print('-------------------------\n')

# 5

import math

print('Задание 5, факториал')
x = eval(input("Факториал какого числа считаем? "))
if (x % 1 == 0 and x >= 0):
    print(math.factorial(x))
else:
    print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')
print('-------------------------\n')

# 6
from random import choice
from string import ascii_uppercase

print('Задание 6, Генерация строки заданной длины и допутимого диапазона')
import random
import string


def randStr(chars=string.ascii_uppercase + string.digits + string.ascii_lowercase, N=0):
    return ''.join(random.choice(chars) for _ in range(N))


print(randStr(N=7))
# По этой ссылке подробно расписано про константы в модуле string
# https://docs-python.ru/standart-library/modul-string-python/strokovye-konstanty-modulja-string/

print('-------------------------\n')

# 7
print('Задание 7, Рассчитывает количество букв верхнего и нижнего регистра')
s = "ПриВет ЕкаТеРина!"
print(f'Букв верхнего регистра: {sum(map(str.isupper, s))}, Букв нижнего регистра: {sum(map(str.islower, s))}')
print('-------------------------\n')

# 8
print('Задание 8, возвращает первые n сторон трегуольника паскаля')


def Pascal(n):
    row = [1]
    for i in range(n):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


n = eval(input('Скольок строк треугольника паскаля вывести?'))
Pascal(n)

print('-------------------------\n')

