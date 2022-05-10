from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = FunctionType(lambda x: x, globals(), 'func')

print(a.__class__, b.__class__, c.__class__)
print(a, b, c)

print(a.__sizeof__(), b.__sizeof__(), c.__sizeof__())
print(c.__sizeof__())

print('*'*10)

from sys import getsizeof

print(getsizeof(a), getsizeof(b), getsizeof(c))

print('*'*10)

import sys

print(sys.getsizeof(a), sys.getsizeof(b), sys.getsizeof(c))

print('*'*10)

import os

print(os.stat('/home/machao/PycharmProjects/Python_Study/Python_Study/Python_Study_1/Python_Study_1_5/Python_Study_1_5_1/Python_Study_1_5_1_1/__init__
