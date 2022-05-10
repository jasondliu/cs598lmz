import types
types.FunctionType.__dict__['__repr__'] = lambda self: '<function %s at 0x%x>' % (self.__name__, id(self))

class C(object): pass

def f():
	def g(): pass

f.__dict__['C'] = C

del f
del g

g = f.C()

print(g)


try:
	import os
	import sys
	sys.path.insert(0, os.path.realpath(__file__))

	import module_file
	print(module_file.f)
	print(module_file.C)

	try:
		print(module_file.g)
	except Exception as e:
		print(e)
except Exception as e:
	print('SKIP')
