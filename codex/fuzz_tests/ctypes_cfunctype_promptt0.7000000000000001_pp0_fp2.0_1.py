import ctypes
# Test ctypes.CFUNCTYPE for multiple return values
from ctypes import *

def callback(*args):
    return args

functype = CFUNCTYPE(c_int, c_int, c_int, c_int)

## Prototype: int func(int a, int b, int c);
func = functype(callback)

print func(1, 2, 3) # (1, 2, 3)
print func(3, 2, 1) # (3, 2, 1)

functype = CFUNCTYPE(c_int, c_int, c_int)

## Prototype: int func(int a, int b);
func = functype(callback)

print func(1, 2) # (1, 2)
print func(2, 3) # (2, 3)

functype = CFUNCTYPE(c_int, c_int)

## Prototype: int func(int a);
func = functype(callback)

print func(1) # (1,)
print func(2) # (2,)

functype =
