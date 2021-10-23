from dotenv import dotenv_values
import math


def get_square(radius):
    return math.pi * radius * radius


config = dotenv_values('.env')
string_radius = config['radius']

try:
    radius = int(string_radius)
except ValueError:
    raise ValueError(f'Не могу превратить значение {string_radius} в число')

if radius <= 0:
    raise ValueError('Радиус круга должен быть больше нуля')

square = get_square(radius)

print(f'Площадь круга радиусом {radius} равна {square}')
