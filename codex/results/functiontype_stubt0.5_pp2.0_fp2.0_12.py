from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(FunctionType))

def func():
    pass

print(type(func))
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print(isinstance(a, types.GeneratorType))
print(type(x for x in range(10)))
print(isinstance(func, types.FunctionType))

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Dog) and isinstance(d, Animal))
print(isinstance(d, Husky))

print(dir('ABC'))
