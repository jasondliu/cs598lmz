from types import FunctionType
list(FunctionType(lambda x: x+1, {}, None, None, None)(1))

def f(x):
    return x+1

# Modules

import math
math.sqrt(2)

# Classes

class C(object):
    def __init__(self, x=0):
        self.x = x
    def g(self, y):
        return self.x + y

c = C(1)
c.g(2)

# Methods

c.g

# Generators

def g():
    for i in range(10):
        yield i

list(g())

# Exceptions

class MyException(Exception):
    pass

try:
    raise MyException()
except MyException:
    print("caught")

# Tracebacks

try:
    1/0
except ZeroDivisionError as e:
    e.__traceback__
    e.__traceback__.tb_frame.f_code

# Coroutines

def coro():
    yield 1
    yield 2

