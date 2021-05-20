# 1

def non_zero_del(var1, var2):
    try:
        result = var1 / var2
    except ZeroDivisionError:
        return "Вы разделили на ноль и перешли на следующий уровень бытия! Поздравляю!"
    else:
        return result


temp = non_zero_del(int(input('Введите делимое:\n')), int(input('Введите делитель:\n')))
print(temp)


# 2


def data_printer(**kwargs) -> str:
    line = ''
    for kw, args in kwargs.items():
        line += f'{kw}: {args}, '
    return line


user_answer_template = {
    'имя': '',
    'фамилия': '',
    'год рождения': '',
    'город проживания': '',
    'адрес эл. почты': '',
    'номер телефона': ''
}

for key in user_answer_template.keys():
    user_answer = input(f'Пожалуйста, введите {key}:\n')
    user_answer_template[key] = user_answer
print(data_printer(**user_answer_template))


# 3

def my_func(first_number: int, second_number: int, third_number: int) -> int:
    if first_number >= second_number:
        if second_number >= third_number:
            return first_number + second_number
        else:
            return first_number + third_number
    else:
        if first_number >= third_number:
            return first_number + second_number
        else:
            return second_number + third_number


numbers = []
while True:
    try:
        user_number = int(input('Введите, пожалуйста, целое число:\n'))
    except ValueError as e:
        print(f'{e}. Это не число, введите число')
    else:
        numbers.append(user_number)
        if len(numbers) > 2:
            break
a, b, c = numbers
print(my_func(a, b, c))


# 4


def my_func(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    result = x
    for _ in range(1, my_func(x, abs(y) - 1)):
        result += x
    return result if y > 0 else 1. / result


# 5


def split_sum():
    end_counter = False
    int_sum = 0
    while not end_counter:
        string = input('Введите, пожалуйста, строку чисел, разделенных пробелом. Если вы хотите остановиться, '
                       'введите ~.\n')
        result_list = list(string.split(' '))
        for el in range(len(result_list)):
            if result_list[el] == '~':
                end_counter = True
                break
            else:
                try:
                    int_sum += int(result_list[el])
                except ValueError as e:
                    print(f'{e} - этот символ не был учтен, поскольку это не число.')
        print(int_sum)


if __name__ == '__main__':
    split_sum()