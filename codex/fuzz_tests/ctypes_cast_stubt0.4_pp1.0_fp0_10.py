import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 实现__len__()和__getitem__()
class Fib(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
f = Fib()
f[0:5]

# __getattr__
class Student(object):
	def __init__(self):
