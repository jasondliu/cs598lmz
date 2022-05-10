from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
def a(x):
    return x
print(a(1))
print(type(a))
print(type(a) == FunctionType)

from types import FunctionType
print(type(FunctionType) == type)
print(type(type))
from types import FunctionType
from functools import wraps
from time import time

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
