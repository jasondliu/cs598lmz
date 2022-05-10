from types import FunctionType
a = (x for x in [1])

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(a, list))

print(isinstance(abs, FunctionType))
print(isinstance(abs, Iterable))
print(isinstance(abs, Iterator))
print(isinstance(abs, Generator))

print(isinstance(range(1), Iterator))
print(isinstance(range(1), Iterable))
print(isinstance(range(1), Generator))

print(isinstance(range(1), list))
print(isinstance(range(1), tuple))

print(isinstance(range(1), FunctionType))

print(isinstance(map(int, [1]), Iterator))
print(isinstance(map(int, [1]), Iterable))
print(isinstance(map(int, [1]), Generator))

print(isinstance(map(int, [1]), FunctionType))
print(isinstance(map(int, [1]), list
