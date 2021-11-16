7.1
7.1.1
flag = True
while flag:
    flag = False
    for i in range(1, len(lwr) - 2, 2):
        if lwr[i] < lwr[i + 2]:
            lwr[i - 1], lwr[i], lwr[i + 1], lwr[i + 2] = lwr[i + 1], lwr[i + 2], lwr[i - 1], lwr[i]
            flag = True
        elif lwr[i] == lwr[i + 2] and lwr[i - 1] > lwr[i + 1]:
            lwr[i - 1], lwr[i + 1] = lwr[i + 1], lwr[i - 1]
            flag = True

is_swap = True
    while is_swap:
        is_swap = False
        for i in range(1, len(lwr) - 2, 2):
            if lwr[i] < lwr[i + 2]:
                lwr[i - 1], lwr[i], lwr[i + 1], lwr[i + 2] = lwr[i + 1], lwr[i + 2], lwr[i - 1], lwr[i]
                is_swap = True
            elif lwr[i] == lwr[i + 2]:
                if lwr[i - 1] > lwr[i + 1]:
                    lwr[i - 1], lwr[i + 1] = lwr[i + 1], lwr[i - 1]
                    is_swap = True

7.1.2
flag = True
    while flag:
        flag = False
        for i in range(n - 2):
            if (data[i + 1] > data[i] > data[i + 2] or
                    data[i] > data[i + 1] and data[i + 1] < data[i + 2]):
                data[i], data[i + 1], data[i + 2] = data[i + 1], data[i + 2], data[i]
                flag = True

is_sort = True
    while is_sort:
        is_sort = False
        for i in range(n - 2):
            if (data[i + 1] > data[i] > data[i + 2] or
                    data[i] > data[i + 1] and data[i + 1] < data[i + 2]):
                data[i], data[i + 1], data[i + 2] = data[i + 1], data[i + 2], data[i]
                is_sort = True

7.1.3
flag1 = True
    for i in range(n):
        if flag1:
            for j in range(n - i):
                if a[-1 - i] > a[-2 - j - i]:
                    a[-1 - i], a[-2 - j - i] = a[-2 - j - i], a[-1 - i]
                    flag1 = False
                    x = -2 - j - i
                    break

is_complete = True
    for i in range(n):
        if is_complete:
            for j in range(n - i):
                if a[-1 - i] > a[-2 - j - i]:
                    a[-1 - i], a[-2 - j - i] = a[-2 - j - i], a[-1 - i]
                    is_complete = False
                    x = -2 - j - i
                    break

7.1.4
flag1 = False
if flag1:
    list_undo.clear()
    list_redo.clear()
    flag1 = False

is_clear_comand = False
if is_clear_comand:
    list_undo.clear()
    list_redo.clear()
    is_clear_comand = False

7.1.5
flag = True
while flag:
    message = input()
    if message == 'quit'
        flag = False
    else:
        print(message)

active = True
while active:
    message = input()
    if message == 'quit'
        active = False
    else:
        print(message)

7.2.
7.2.1
import random

x = []
N = int(input('Введите число 1..50: '))
flag = True
for i in range(100):
    x.append(random.randint(1, 50))


for i in range(100):
    if N == x[i]:
        flag = False
        print('Введенное число находится в массиве под индексом', i)
        break

if flag:
    print('Число не найдено!')

import random

x = []
N = int(input('Введите число 1..50: '))
found = False
for i in range(100):
    x.append(random.randint(1, 50))


for i in range(100):
    if N == x[i]:
        found = True
        print('Введенное число находится в массиве под индексом', i)
        break

if not found:
    print('Число не найдено!')