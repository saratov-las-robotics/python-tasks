from dotenv import dotenv_values
from random import uniform, choice


def read_env_float(name):
    as_string = config[name]
    as_value = float(as_string)
    return as_value


def get_any_curse():
    curses = [
        'ну',
        'типа',
        'хз',
        'этава',
        'блин',
    ]

    return choice(curses)


def patch_text(text, chance):
    words = text.split()
    patched = list()
    patched.append(words[0])

    for word in words[1:]:
        roll = uniform(0, 1)

        if roll < chance:
            curse = get_any_curse()
            patched.append(f', {curse},')

        patched.append(word)


    return ' '.join(patched).replace(' , ', ', ').replace(',,', ',')


config = dotenv_values('.env')
text = config['text']
curse_chance = read_env_float('curse_chance')
result_text = patch_text(text, curse_chance)

print(result_text)
