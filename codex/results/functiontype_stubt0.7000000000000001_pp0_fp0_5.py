from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(a)
print(isinstance(abs, FunctionType))

class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class Runnable(object):
	pass

class Flyable(object):
	pass

class Dog(Mammal, Runnable):
	pass

class Bat(Mammal, Flyable):
	pass

class Parrot(Bird, Flyable):
	pass

class Ostrich(Bird, Runnable):
	pass

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

import types
def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for
