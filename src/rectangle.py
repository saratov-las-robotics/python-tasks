from dotenv import dotenv_values


def read_env_int(name):
    as_string = config[name]
    as_value = int(as_string)
    return as_value


def get_square(width, height):
    return width * height


config = dotenv_values('.env')
width = read_env_int('width')
height = read_env_int('height')
square = get_square(width, height)

print(f'Площадь прямоугольника {width}x{height} равна {square}')
