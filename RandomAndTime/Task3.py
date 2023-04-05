"""
На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
участники должны распределяться между забегами случайным образом.
Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор, пока не будет введено «off».
После генерации каждого номера должно печататься:
1) «Ваш номер: _».
2) «Участников в первом забеге: _», «Участников во втором забеге: _».
"""
from random import randint
n = [0,0]
while True:
	if input() == 'off': break
	a = randint(1,2)
	n[a-1] += 1
	print(f'Ваш номер: {a}\nУчастников в первом забеге: {n[0]}, Участников во втором забеге: {n[1]}')