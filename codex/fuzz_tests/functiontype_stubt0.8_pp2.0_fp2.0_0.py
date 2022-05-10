from types import FunctionType
a = (x for x in [1])
print('a', type(a), isinstance(a, Iterator))
print('a', type(a), isinstance(a, Iterable))
# <class 'generator'> True False
print(isinstance(a, Generator))
# True
print(isinstance(a, FunctionType))
