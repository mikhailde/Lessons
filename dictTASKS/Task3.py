"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
data = {}
while True:
	str = input().split(',')
	if str[0] == 'off': break
	data[tuple([i for i in str[:2] if i != 'off'])] = str[2]
print(data)