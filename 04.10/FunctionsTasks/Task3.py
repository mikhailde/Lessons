"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""
def passage(score):
		print(score>50)
		return score>50
for i in range(int(input('Введите число учеников: '))):
	if passage(int(input('Введите свой балл: '))) == False:
		print('Вы отчислены')
