from dotenv import dotenv_values
import math


def get_square(radius):
    return math.pi * radius * radius


config = dotenv_values('.env')
string_radius = config['radius']
radius = int(string_radius)
square = get_square(radius)

print(f'Площадь круга радиусом {radius} равна {square}')
