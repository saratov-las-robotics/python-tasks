def megillah(input):
	return f'Все говорят "{input.lower()}", а ты возьми и купи бычка'


print('Ты не хочешь ли купить бычка?')
print('> ', end='')
text = input()
answer = megillah(text)
print(answer)

while True:
	print('> ', end='')
	text = input()
	answer = megillah(text)
	print(answer)