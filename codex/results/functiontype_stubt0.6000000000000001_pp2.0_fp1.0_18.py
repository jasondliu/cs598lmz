from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)

def add(a, b):
    return a + b

print(add)
print(type(add))
print(type(add) == FunctionType)
print(type(add) == type(lambda a, b: a + b))

print(type(abs) == types.BuiltinFunctionType)
print(type(lambda a, b: a + b) == types.LambdaType)
print(type(x for x in [1, 2, 3]) == types.GeneratorType)

print(dir(a))
print(a.__iter__)
print(a.__iter__() == iter(a))

print(a.__next__)
print(a.__next__() == next(a))
print(next(a))

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self
