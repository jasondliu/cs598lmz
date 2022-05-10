from types import FunctionType
list(FunctionType(x,globals(),name='x'))

exit()

import inspect
def log(fn):
	if inspect.isgeneratorfunction(fn):
		def wrapper(*args , **kwargs):
			return log(fn(*args , **kwargs))
		return wrapper
	def wrapper():
		print 'call' , fn.__name__ , '()'
		return fn()
	return wrapper

@log
def now():
	print '2013\n'

now()

@log
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n+1

fib(3)

'''
import inspect
def log(fn):
	def wrapper():
		print 'call' , fn.__name__ , '()'
		return fn()
	return wrapper

def log(fn):
	def wrapper(*args,**kw):
		print 'call' , fn
