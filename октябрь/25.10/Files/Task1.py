"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""
with open('1.txt', 'w+') as f:
	f.write('Я гений и стараюсь учить питон')
	f.seek(0)
	print(f.read(7))
