from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, object))

print()

class A(object):
    def __init__(self):
        pass
    def __iter__(self):
        return self
    def __next__(self):
        return 1

a = A()
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, object))

print()

class A(object):
    def __init__(self):
        pass
    def __iter__(self):
        return self
    def __next__(self):
        return 1

a = A()
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, object))


