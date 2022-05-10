from types import FunctionType
a = (x for x in [1])
print isinstance(a, GeneratorType)
print type(a)
b = {'a':1, 'b':2}

print type(b)

print isinstance(b, dict)

print isinstance('ls', str)

def f():
	pass

print type(f)
print isinstance(f, FunctionType)
