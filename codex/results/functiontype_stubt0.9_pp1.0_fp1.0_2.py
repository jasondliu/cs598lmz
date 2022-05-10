from types import FunctionType
a = (x for x in [1])
print(type(a))
# <class 'generator'>
b = []
print(type(b))
# <class 'list'>
c = []
print(type(c))
# <class 'list'>
print(isinstance(b, Iterable))
# True
print(isinstance(b, Iterator))
# False
print(isinstance(a, Iterable))
# True
print(isinstance(a, Iterator))
# True
