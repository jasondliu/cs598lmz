from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)

def add(x, y):
	return x + y
a = FunctionType(add.__code__, add.__globals__, name = 'add', argdefs = (1, 1), closure = add.__closure__)
print(a(1, 1))
