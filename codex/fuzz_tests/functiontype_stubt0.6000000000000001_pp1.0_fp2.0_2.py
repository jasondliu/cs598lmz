from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == FunctionType)
print(type(a) == type(len))
print(type(a) == type(type))
print(type(a) == type(lambda x: x))

print('-' * 20)

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, list))
print(isinstance(a, tuple))
