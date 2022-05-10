from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(a, list))

print('-----------------------------------')

print(isinstance(iter(a), Iterator))
print(isinstance(iter(a), Iterable))
print(isinstance(iter(a), Generator))
print(isinstance(iter(a), FunctionType))
print(isinstance(iter(a), list))

print('-----------------------------------')

b = [1, 2, 3]
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, Generator))
print(isinstance(b, FunctionType))
print(isinstance(b, list))

print('-----------------------------------')

print(isinstance(iter(b), Iterator))
print(isinstance(iter(b), Iterable))
print(isinstance(iter(b), Generator))
print(isinstance(iter(b), FunctionType))

