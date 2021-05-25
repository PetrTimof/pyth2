# 1

from sys import argv


script_name, work_load, per_hour, benefit = argv
print("Название программы: ", script_name)
print('Выработка в часах: ', work_load)
print('Ставка в час: ', per_hour)
print('Премия: ', benefit)
print('Всего заработная плата: ', int(work_load) * int(per_hour) + int(benefit))

# 2


from random import randint

source_list = [randint(0, 1000) for i in range(30)]
print(f'Исходный список: {source_list}')
result_list = [el for index, el in enumerate(source_list) if index > 0 and el > source_list[index - 1]]
print(f'Результат: {result_list}')


# 3


print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])


# 4


from random import randint

source_list = [randint(0, 10) for i in range(20)]
print(f'Исходный список: {source_list}')
result = [el for el in source_list if source_list.count(el) == 1]
print(f'В списке не повторяются числа: {result}')


# 5


from functools import reduce


def func(prev_el, el):
    return prev_el * el


source_list = [el for el in range(100, 1001) if el % 2 == 0]
print(source_list)
print(f'Произведение всех элементов: {reduce(func, source_list)}')

#6.1

def generator(start):
    for el in count(start):
        yield el


start = None
while True:
    if start == None:
        try:
            start = int(input('С какого числа начинаем генерацию? - '))
            list = generator(start)
        except ValueError:
            print('Введите число')
    else:
        key = input('Для генерации нажмите Enter, для выхода любой символ - ')
        if key == '':
            print(f'Сгенерированное число равно: {next(list)}')
        else:
            break

#6.2


from itertools import cycle
from random import randint

source_list = [randint(0, 10) for i in range(5)]
print(f'Исходный список: {source_list}')
i = 0
for el in cycle(source_list):
    print(el, end=' ')
    if i > 50:
        break
    i += 1


#7


from itertools import count

def generator():
    for el in count(1):
        result = el
        for _ in range(1, el):
            result *= _
        yield result

i = 0
for el in generator():
    if i == 15:
        break
    print(el)
    i += 1

