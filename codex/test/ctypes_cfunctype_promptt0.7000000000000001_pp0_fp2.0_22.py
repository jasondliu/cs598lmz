import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is not good enough: it just checks whether it crashes in the
# presence of ctypes. I'd like to check that it has the right effect, but
# how can I do that?
import sys
import weakref

def func(a, b):
    return a+b

class MyClass:
    pass

