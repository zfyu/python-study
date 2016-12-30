# -*- coding: utf-8 -*-
def fact(n):
	'''
		fact doctest
		
		>>> fact(1)
		1
		>>> fact(3)
		6
		>>> fact(0)
		Traceback (most recent call last):
			...
		ValueError
	'''
	if n < 1:
		raise ValueError()
	if n == 1:
		return 1
	return n*fact(n-1)
if __name__ == '__main__':
	import doctest
	doctest.testmod()