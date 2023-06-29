from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculates_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Сравнивает число с 0."""
    if your_number <= 0:
        return
    else:
        print(f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {calculates_square_root(your_number)}')


print(message)
calc(25.5)
