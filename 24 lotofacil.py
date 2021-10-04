Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.randint(0,10)
2
>>> random.randint(1,25)
14
>>> def lotofacil():
	jogo = []
	while len(jogo) < 15:
		num = random.randint(1,25)
		if num in jogo:
			continue
		else:
			jogo.append(num)
	print(jogo)

	
>>> lotofacil()
[16, 13, 19, 5, 22, 7, 11, 23, 4, 24, 8, 25, 3, 10, 17]
>>> def lotofacil():
	jogo = []
	while len(jogo) < 15:
		num = random.randint(1,25)
		if num in jogo:
			continue
		else:
			jogo.append(num)
	print(sorted(jogo))

	
>>> lotofacil()
[2, 3, 4, 5, 8, 9, 10, 12, 13, 16, 17, 18, 19, 21, 23]
>>> 