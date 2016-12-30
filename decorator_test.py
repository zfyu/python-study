import functools
def log(str_or_func):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			fname = func.__name__
			print('%s call %s():'%(text,fname))
			func(*args,**kw)
			print('end call %s():'%fname)
		return wrapper
	if isinstance(str_or_func,str):
		text = str_or_func
		return decorator
	else:
		text = 'begin'
		return decorator(str_or_func)

@log
def f():
	print('abc')
	
f()

@log('execute')
def g():
	print('xyz')
	
g()
