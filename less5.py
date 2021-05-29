# 1

with open('task1_file.txt', 'w', encoding='UTF-8') as f:
    while True:
        print('Введите данные. Для окончания ввода нажмите Enter')
        line = input()
        if line:
            f.write(line + '\n')
        else:
            break


# 2


with open('task2_file.txt', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f, 1):
        print(f'Строка - {i}, слов - {len(line.split(" "))}')


# 3


with open('task3_file.txt', 'r', encoding='UTF-8') as f:
    persons = list(map(lambda line: tuple(line.replace('\n', '').split(' ')), f.readlines()))
print(persons)
print(f'Сотрудники с окладом менее 20 000: {[person[0] for person in persons if int(person[1]) < 20000]}')
print(f'Средний доход: {sum([int(person[1]) for person in persons])/len(persons)}')


# 4


items = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task4_file_new.txt', 'w', encoding='UTF-8') as fnew:
    with open('task4_file.txt', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '').split(' - ')
            fnew.write(f'{items[line[0]]} - {line[1]}\n')


# 5


from random import randint

items = [randint(0, 10) for _ in range(5)]
with open('task5_file.txt', 'w', encoding='UTF-8') as f:
    f.write(' '.join(map(str, items)))
print(f'Числа: {items}')
print(f'Сумма чисел: {sum(items)}')


# 6


def to_int(value):
    value = ''.join([el for el in list(value) if el.isdigit()])
    return int(value) if value.isdigit() else 0

dict = {}
with open('task6_file.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.replace('\n', '').split(' ')
        dict[line[0]] = sum([to_int(el) for el in line[1:]])
    print(dict)


#7


import json

with open('task7_file.txt', 'r', encoding='UTF-8') as f:
    firms = {}
    for line in f:
        attr = line.replace('\n', '').split(' ')
        firms[attr[0]] = int(attr[2]) - int(attr[3])
    profits = [int(el[1]) for el in firms.items() if el[1] > 0]
    list = [firms, {'average_profit': sum(profits) / len(profits)}]
with open('task7_file.json', 'w', encoding='UTF-8') as jf:
    json.dump(list, jf)
