# 1

class Matrix:

    def to_str(self, my_list):
        return '\n'.join([' '.join(list(map(str, el))) for el in my_list])

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return self.to_str(self.matrix)

    def __add__(self, other):
        all_list = []
        for i, m_list in enumerate(self.matrix):
            row = []
            for j, el in enumerate(m_list):
                row.append(el + other.matrix[i][j])
            all_list.append(row)
        return self.to_str(all_list)

matr_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matr_2 = Matrix([[6, 7, 2], [9, 8, 5], [9, 8, 7]])
print(matr_1)
print('----------')
print(matr_2)
print('----------')
print(matr_1 + matr_2)


# 2


from abc import ABC, abstractmethod

# класс одежда
class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption

# класс пальто
class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return self.param / 6.5 + 0.5

# класс костюм
class Suit(Clothes):

    @property
    def fabric_consumption(self):
        return 2 * self.param + 0.3

coat = Coat(13)
print(f'Расход ткани на пальто: {coat.fabric_consumption}')

suit = Suit(4)
print(f'Расход ткани на костюм: {suit.fabric_consumption}')

print(f'Общий расход ткани на пальто и костюм: {coat + suit}')


# 3


class Cell:

    def __init__(self, cells = 0):
        self.cells = cells

    def __str__(self):
        return f'Клетка с количеством ячеек - {self.cells}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells) if self.cells > other.cells else 'Количество ячеек первой клетки меньше, чем второй'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, row):
        return '\n'.join(['*' * row for i in range(0, self.cells // row)] + ['*' * (self.cells % row)])


cel_1 = Cell(17)
cel_2 = Cell(3)
print(f'Сумма: {cel_1 + cel_2}')
print(f'Разность: {cel_1 - cel_2}')
print(f'Произведение: {cel_1 * cel_2}')
print(f'Деление: {cel_1 / cel_2}')
print(f'Ячейки по рядам:\n{cel_1.make_order(5)}')