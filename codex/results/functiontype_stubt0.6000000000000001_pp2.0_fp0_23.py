from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a)
print(type(a))
print(type(b))
print(a == b)
print(a is b)
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

print("-------")

def foo():
    yield 1
    yield 2

b = foo()
print(b)
print(type(b))
print(isinstance(b, FunctionType))
print(isinstance(b, GeneratorType))

print("-------")

import types
def foo():
    yield 1
    yield 2

b = foo()
print(b)
print(type(b))
print(isinstance(b, types.FunctionType))
print(isinstance(b, types.GeneratorType))

print("-------")

import types
class Foo:
    def __init__(self):
        self.a = 1
        self.b = 2

f = Foo()
print(f)
print(type(f))
print(isinstance(f,
