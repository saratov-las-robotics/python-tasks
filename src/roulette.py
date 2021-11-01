import random


def roulette():
	roll = random.randint(1, 3)

	if (roll == 1):
		raise ValueError('Не ладно')
	else:
		return 'Ладно'


while True:
	roulette()
