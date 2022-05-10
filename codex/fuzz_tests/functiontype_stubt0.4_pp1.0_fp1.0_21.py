from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(a) == GeneratorType)
print(type(print) == FunctionType)

print(type(abs) == FunctionType)
print(type(lambda x: x) == FunctionType)
print(type(x for x in range(10)) == GeneratorType)
print(type((x for x in range(10))) == GeneratorType)
print(type([x for x in range(10)]) == GeneratorType)
print(type(100) == int)

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
