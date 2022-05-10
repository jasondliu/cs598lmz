from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(aa, GeneratorType))

print(type(a.__iter__()))


print(isinstance(lambda x: x, FunctionType))

def func():
	pass
print(isinstance(func, FunctionType))

import types
print(types.FunctionType)

def add(x, y, f):
	return f(x) + f(y)

print(add(-5, 6, abs))

from functools import reduce
def fn(x, y):
	return x * 10 + y
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))
print(str2int('
