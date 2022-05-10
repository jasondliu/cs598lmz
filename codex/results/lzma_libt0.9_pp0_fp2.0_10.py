import lzma
lzma.compress # success!

from sys import getsizeof
getsizeof('x' * 5)
str.__sizeof__(str) # __sizeof__ doesn't work for most types :(
int.__sizeof__(int)

a = tuple(zip(range(10),range(10)))
b = tuple(zip(range(10),range(10)))
getsizeof(a) # 48
getsizeof(b) # 48

a == b # True
a is b # False
a and b == (0, 0) # True
a and b is (0, 0) # False
a[0] == b[0] # True
a[0] is b[0] # False

from numbers import Number
class Point(tuple):
	'''<x,y>'''
	def __new__(cls, x, y):
		return tuple.__new__(cls, (x,y))
	@property
	def x(self): return self[0]
	@property
	def y(self): return self[1]
