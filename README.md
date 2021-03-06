# Python tasks

> Если всё получилось - приступайте к [части 2](README_2.md)

1. Поставьте python 3 - по идее, у всех должен стоять и так
2. Установите [poetry](https://github.com/python-poetry/poetry):
   1. Самый простой способ - открыть powershell и выполнить в нём следующий код. Он скачает и установит poetry. 
      
      `(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -`
3. Перейдите в корень своего репозитория `/`
4. Инициализируйте poetry: `poetry init`. Она спросит несколько вопросов; на вопрос про интерактивную установку пакетов дважды ответьте "no".
5. Добавьте dotenv: `poetry add python-dotenv`
6. Создайте файл [`/.env`](/.env)
   1. Напишите в него `radius=2`
7. Скопируйте мой файл [/src/circle.py](/src/circle.py) и запустите его: `poetry run python src/circle.py`. Если программа отработает корректно - то вы настроили всё правильно, дальше ковыряйте задания. Оформлять можно как угодно: хотите каждое задание в отдельном файле - пожалуйста. Хотите всё в одном - удачи.

Отдельно обращу внимание на следующее. Запускать команду `poetry run python src/circle.py` надо из директории `/`, не из `/src` - иначе файл `.env` не будет найден. 

## Требования
- передавать входные параметры через `.env`
- выводить результат работы функций в консоль с пояснениями
- не писать функций, которые возвращают ничто
- писать нормальный код: не сокращайте `radius` до `r` и пр. Тыкаясь пальцем в небо, вы со временем поймёте, что такое "нормальный"

Совет: пишите код постепенно. Я на лекции начал с условно плохой программы и закончил условно хорошей - и это удобный путь. Напишите сначала самую тупую версию, чтобы она заработала; и улучшайте код постепенно, шаг за шагом. Так вы сможете добавлять сложность не сразу одним махом, а порционно.

Дзена вы достигните тогда, когда поймёте, что нет хорошего кода. Улучшать можно бесконечно.

## Задачи

Далее я буду обозначать символом `>` входные данные, а символом `<` - выходные. То есть запись
```
> 1
< 2
```
означает "на вход функции подали 1, а на выходе получили 2".

Естетсвенно, если у вас есть задачи с уроков информатики - тоже пишите их сюда, обсудим.


### 1. Прямоугольник

Написать функцию с сигнатурой `(number, number) => number`, которая
- принимает на вход длину и ширину прямоугольника
- возвращает площадь прямоугольника
```
> 2, 3
< 6
```

### 2. Квадрат

Написать функцию с сигнатурой `(number) => string`, которая
- принимает на вход длину стороны квадрата
- возвращает квадрат указанного размера из символов `*`
```
> 3
< ***
  ***
  ***

> 1
< *

> 4
< ****
  ****
  ****
  ****
```

##### Дополнения:
- Такие строчки собираются через символ переноса строки `\n`. То есть,
```python
> print('**\n**')
< **
  **
```
- Цикл будет удобно написать так, но я не настаиваю:

```python
for i in range(1, n):
    # выполнится n раз
```


### 3. Сумма

Написать функцию с сигнатурой `() => number`, которая
- возвращает сумму чисел от 0 до 500 включительно


### 4. Нублинка

Перед этой задачей сделайте [часть 3](README_3.md) - там чутка объяснено, как работать с вероятностями и массивами.

Написать функцию с сигнатурой `(string, number) => string`, которая
- принимает на вход текст и вероятность (дробное число от 0 до 1)
- с этой вероятностью функция вставляет в текст слова-паразиты: "ну", "блин", "короче" и так далее (не вульгарные, добавлять свои можно)
- функция возвращает текст со словами-паразитами

```
> 'выводить результат работы функций в консоль', 0.5
< 'выводить, короче, результат работы, ну, функций в консоль, блин'
```

##### Дополнения:
- работать с вероятностью можно так:
```python
from random import uniform

# chance - ваша вероятность
def foo(chance):
    random_value = uniform(0, 1)

    if chance < random_value:
        # повезло
    else:
        # не повезло
```

- пересобрать текст можно разными способами, я предлагаю такой:
```python
def foo(text):
    words = text.split(' ') # разделить строку на массив слов

    # ... что-то с ним сделать

    return ' '.join(words) # сшить строку из массива слов обратно
```
