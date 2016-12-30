def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x

def power(x,n):
	s=1
	while n>0:
		n = n-1
		s=s*x
	return s