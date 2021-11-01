import string
import random


def sort_by_alphabet(word):
	return word[0].lower()

def sort_by_length(word):
	return len(word)


def get_any_string(length):
	letters = string.ascii_uppercase + string.digits + string.ascii_lowercase
	return ''.join(random.choices(letters, k=length))


def get_array(length = 10):
	words = []

	for i in range(0, length):
		word_length = random.randint(3,15);
		word = get_any_string(word_length)
		words.append(word)

	return words


arr = get_array()

random.shuffle(arr)
print('Перемешанный массив:', arr)

arr.sort(key=sort_by_alphabet)
print('Отсортированный по алфавиту', arr)

arr.sort(key=sort_by_length, reverse=True)
print('Отсортированный по убыванию длины строки', arr)