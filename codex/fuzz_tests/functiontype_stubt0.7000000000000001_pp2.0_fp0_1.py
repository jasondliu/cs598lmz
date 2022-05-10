from types import FunctionType
a = (x for x in [1])
print(type(a))
b = (x for x in [1])
print(type(b))
print(a == b)
print(a is b)

def is_iterable(param):
    return isinstance(param, Iterator)

def is_iterable(param):
    return isinstance(param, Iterator)

def is_iterable(param):
    return isinstance(param, Iterator)

print(is_iterable([]))
print(is_iterable({}))
print(is_iterable(100))

def is_iterable(param):
    return hasattr(param, '__iter__')

print(is_iterable([]))
print(is_iterable({}))
print(is_iterable(100))
print(is_iterable(iter([])))
print(is_iterable(iter({})))
print(is_iterable(iter(100)))

# 判断是否可以迭代
from collections import Iterator
def is_iterable(param
