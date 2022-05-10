import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(x):
    return x*x
f = FUNTYPE(func)
print(f(3))

print("==============================")

import ctypes
import ctypes.util
libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.printf("Hello, %s!\n", b"world")

print("==============================")

import ctypes
libc = ctypes.CDLL("/lib/libc.so.6")
libc.printf("Hello, %s!\n", b"world")

print("==============================")

import ctypes
libc = ctypes.CDLL(None)
libc.printf("Hello, %s!\n", b"world")

print("==============================")

import ctypes
libc = ctypes.CDLL("libc.so.6")
libc.printf("Hello, %s!\n", b"world")

print("==============================")

import ctypes

