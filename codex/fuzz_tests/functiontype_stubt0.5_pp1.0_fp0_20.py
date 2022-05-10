from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))
print(type(a.__await__))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, object))

print('****************')

def test_gen():
    yield 1

b = test_gen()
print(type(b))
print(type(b.__next__))
print(type(b.__iter__))
print(type(b.send))
print(type(b.throw))
print(type(b.close))
print(type(b.__await__))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, object))

print('****************')

class TestGen:
    def __init__(self):
        self.x = 1

   
