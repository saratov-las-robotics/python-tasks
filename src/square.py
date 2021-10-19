from dotenv import dotenv_values


def read_env_int(name):
    as_string = config[name]
    as_value = int(as_string)
    return as_value


def get_square(length):
    value = ''

    for _ in range(0, length):
        value += '*' * length
        value += '\n'

    return value


config = dotenv_values('.env')
length = read_env_int('length')
square = get_square(length)

print(square)
