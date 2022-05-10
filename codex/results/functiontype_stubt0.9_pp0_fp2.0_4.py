from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, collections.Iterable))  # True
print(isinstance(a, collections.Iterator))  # True
b = [1, 2]
print(isinstance(b, collections.Iterable))  # True
print(isinstance(b, collections.Iterator))  # False
