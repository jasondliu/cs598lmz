from types import FunctionType
list(FunctionType(func.__code__,globals(),name='function'))

def f(x):
	return 2*x

def func():
	return map(f,list(range(3)))

list(FunctionType(func.__code__,{'f':f},name='function'))


def f(x):
	return 2*x

def func():
	return map(f,list(range(3)))

f_new = FunctionType(func.__code__,{'f':f},name='function')



class A(object):
	def __init__(self,x=0):
		self.x = x

class B(A):
	def __init__(self,x=0,y=0):
		self.y = y
		A.__init__(self,x)

def foo(x):
	print(x)

def bar(x):
	return foo(x)

def func():
	b = B(1,2)
	return b

import types
def intercept_attr
