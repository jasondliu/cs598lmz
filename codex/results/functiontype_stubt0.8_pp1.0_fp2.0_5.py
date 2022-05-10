from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))
print(type(a))
print(isinstance(lambda x: x, FunctionType)) #True
print(isinstance(x for x in [1], Iterator)) #True
print(isinstance(abs, FunctionType)) #True
print(isinstance(iter, FunctionType)) #True
print(isinstance([], Iterator)) #False
print(isinstance([], Iterable)) #True

'''

"""
def g():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def fibonacci(n):
    a, b, i = 0, 1, 0
    while i < n:
        yield a
        a, b = b, a + b
        i = i + 1
    return "done"

f = fibonacci(10)

print(f)

for i in f:
    print(i)

#next(f)

"""

"""
# 迭代器
from collections import Iterable
from collections import Iterator


