import ctypes
# Test ctypes.CFUNCTYPE()

from ctypes import *

# void func(int)
FUNC = CFUNCTYPE(None, c_int)

def func(n):
    print "func(%d)" % n

f = FUNC(func)

f(42)

# void func2(int, int)
FUNC2 = CFUNCTYPE(None, c_int, c_int)

def func2(n, m):
    print "func2(%d, %d)" % (n, m)

f = FUNC2(func2)

f(42, 17)

# int func3(int)
FUNC3 = CFUNCTYPE(c_int, c_int)

def func3(n):
    return n + 100

f = FUNC3(func3)

print f(42)

# int func4(int, int)
FUNC4 = CFUNCTYPE(c_int, c_int, c_int)

def func4(n, m):
    return n + m
