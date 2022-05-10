import ctypes
ctypes.cast(0, ctypes.py_object)

# Code type object
import dis
dis.opname[100]

# Frame object
def f(): pass
def g(x): pass
f.__code__
f.__code__.co_varnames
f.__code__.co_argcount
g.__code__.co_varnames
g.__code__.co_argcount

# Function type object
def h(x, y):
	return x + y
h.__code__.co_varnames
h.__code__.co_argcount

# Method type object
class A:
	def m(self, x, y):
		return x + y
A.m.__code__.co_varnames
A.m.__code__.co_argcount

# Generator type object
def f():
	yield 1
	yield 2
f.__code__.co_varnames
f.__code__.co_argcount

# Traceback object
import sys
try:
	1 / 0
except
