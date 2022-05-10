from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(a)
print(b)
print(type(a))
print(type(b))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(a, Sequence))
print(isinstance(b, Sequence))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(a, Mapping))
print(isinstance(b, Mapping))

print("\n\n")

def func():
    yield 1
c = func()
print(c)
print(isinstance(c, GeneratorType))
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))
print(isinstance(c, Sequence))
print(isinstance(c, FunctionType))
print(isinstance(c,
