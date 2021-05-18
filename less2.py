# 1

my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4], (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10}, \
frozenset(), range(11), b'twelwe', bytearray(b'thirteen'), zip(*[(14,15), (16,17), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")

# 2

my_list = list(input("Введите числа без пробела - "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i -1]

print(my_list)

# 3

month = int(input("Введите номер месяца:" ))

month_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", \
              9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", \
              "ноябрь", "декабрь"]
year_time = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

if month in month_dict:
    print(f"{month} месяц - это {month_dict[month]}")
else:
    print("Неправильное число")

month_num = month

if month_num in sum(year_time.values(),[]):
    for i in year_time.items():
        if month_num in i[1]:
            print(i[0])


# 4

string = input("Введите число с пробелом").split()

for n, i in enumerate(string, 1):
    print(n, i) if len(i) <= 10 else print(n, (i[:10]))

# 5

my_list = [9, 6, 5, 5, 6, 4, 4, 6, 7, 5, 3, 4, 5]
new_number = int(input("Введите новый элемент рейтинга "))
i = 0
for n in my_list:
    if new_number <= n:
        i + 1
my_list.insert(i, new_number)
print(my_list)