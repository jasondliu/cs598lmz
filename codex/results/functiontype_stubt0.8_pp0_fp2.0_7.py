from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))
print(isinstance(a, object))
print(isinstance(a, type))

def f():
    yield 1
print(isinstance(f(), GeneratorType))

a = (x for x in [1])
print(isinstance(f(), Iterator))

def f():
    yield 1
print(isinstance(f(), Iterable))


class A:
    pass

print(isinstance(A(), A))
print(isinstance(A(), object))
print(isinstance(A(), type))
print(isinstance(A(), FunctionType))
print(isinstance(A(), str))
print(isinstance(A(), bytearray))

a = A()
print(isinstance(a, A))
print(isinstance(a, object))
print(isinstance(a, type))
print(isinstance(a, FunctionType))
print(isinstance(a,
