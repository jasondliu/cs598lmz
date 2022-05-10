import ctypes
ctypes.cast(5, ctypes.py_object)

int('1') + int('2')

import math

def my_sqrt(a):
    if a < 0:
        raise ValueError('a is negative')
    if a == 1:
        return 1.0
    else:
        return math.sqrt(a)

my_sqrt(1)
my_sqrt(2)
