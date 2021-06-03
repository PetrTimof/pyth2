# 1

import time
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.__color = None

    def running(self):
        for item in cycle([('red', 7), ('yellow', 2), ('green', 10), ('yellow', 2)]):
            self.__color = item[0]
            print(self.__color)
            time.sleep(item[1])

obj = TrafficLight()
obj.running()


# 2


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        return f'Для покрытия всего дорожного полотна необходимо: {self._length * self._width * 25 * 5 / 1000} тонн асфальта'

rd = Road(5000, 10)
print(rd.weight())


# 3


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

pos1 = Position('Иван', 'Иванов', 'Директор', 50000, 30000)
print(f'Полное имя: {pos1.get_full_name()}')
print(f'Доход с учетом премии: {pos1.get_total_income()}')

pos2 = Position('Петров', 'Фёдор', 'Зам.директора', 40000, 20000)
print(f'Полное имя: {pos2.get_full_name()}')
print(f'Доход с учетом премии: {pos2.get_total_income()}')


# 4


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('Car went')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        print(f'Car turned {direction}')

    def show_speed(self):
        print(f'Current speed of the car: {self.speed}')

class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(0, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Current speed of the car: {self.speed}. Attention!!! High speed')
        else:
            super().show_speed()

class SportCar(Car):

    def __init__(self, color, name):
        super().__init__(0, color, name, False)

class WorkCar(Car):

    def __init__(self, color, name):
        super().__init__(0, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Current speed of the car: {self.speed}. Attention!!! High speed')
        else:
            super().show_speed()

class PoliceCar(Car):

    def __init__(self, color, name):
        super().__init__(0, color, name, True)

town = TownCar('Green', 'TownCar name')
town.go()
town.speed = 30
town.show_speed()
town.turn('right')
town.speed = 70
town.show_speed()
print(f'Attributes: name - {town.name}, color - {town.color}, speed - {town.speed}, is_police - {town.is_police}')
town.stop()

print('**********************************')

sport = SportCar('Red', 'SportCar name')
sport.go()
sport.speed = 50
sport.show_speed()
sport.turn('left')
sport.speed = 150
sport.show_speed()
print(f'Attributes: name - {sport.name}, color - {sport.color}, speed - {sport.speed}, is_police - {sport.is_police}')
sport.stop()

print('**********************************')

work = WorkCar('Yellow', 'WorkCar name')
work.go()
work.speed = 20
work.show_speed()
work.turn('left')
work.speed = 50
work.show_speed()
print(f'Attributes: name - {work.name}, color - {work.color}, speed - {work.speed}, is_police - {work.is_police}')
work.stop()

print('**********************************')

police = PoliceCar('Blue', 'PoliceCar name')
police.go()
police.speed = 40
police.show_speed()
police.turn('right')
police.speed = 80
police.show_speed()
print(f'Attributes: name - {police.name}, color - {police.color}, speed - {police.speed}, is_police - {police.is_police}')
police.stop()


# 5


class Stationery:

    def __init__(self, title):
        self.title = title
        print(f'Создан объект: {self.title}')

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('Инструмент ручка')

class Pencil(Stationery):

    def draw(self):
        print('Инструмент карандаш')

class Handle(Stationery):

    def draw(self):
        print('Инструмент маркер')

stat = Stationery('Канцелярская принадлежность')
stat.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()
