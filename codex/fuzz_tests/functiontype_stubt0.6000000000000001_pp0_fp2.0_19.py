from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def a():
	yield 1
a = a()
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def a():
	yield from [1]
a = a()
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def a():
	yield 1
a = a()
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
