from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(b, IteratorType))
print(isinstance(a, IteratorType))
print(isinstance(b, Iterable))
print(isinstance(a, Iterable))

print(isinstance(lambda x: x, FunctionType))

def f():
    print("hello")

print(isinstance(f, FunctionType))
