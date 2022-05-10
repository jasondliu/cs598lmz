from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))

def f():
    yield 1

print(isinstance(f(), FunctionType))

print(isinstance(f, FunctionType))

print(isinstance(f, GeneratorType))

print(isinstance(f(), GeneratorType))

print(isinstance(f, IteratorType))

print(isinstance(f(), IteratorType))

print(isinstance(f, IterableType))

print(isinstance(f(), IterableType))

print(isinstance(f, IteratorType))

print(isinstance(f(), IteratorType))

print(isinstance(f, IterableType))

print(isinstance(f(), IterableType))

print(isinstance(f, IteratorType))

print(isinstance(f(), IteratorType))

print(isinstance(f, IterableType))

print(isinstance(f(), IterableType))

print(isinstance(f, IteratorType))

print(isinstance(f(), IteratorType))

print(is
