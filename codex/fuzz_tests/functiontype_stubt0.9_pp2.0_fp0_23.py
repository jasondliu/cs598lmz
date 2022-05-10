from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
