import ctypes
# Test ctypes.CFUNCTYPE(None)

import ctypes

functype = ctypes.CFUNCTYPE(None)

def test(func):
    func()

@functype
def func():
    pass

test(func)

# Test ctypes.CFUNCTYPE(None, ctypes.c_int)

import ctypes

functype = ctypes.CFUNCTYPE(None, ctypes.c_int)

def test(func):
    func(42)

@functype
def func(value):
    print(value)

test(func)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

import ctypes

functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test(func):
    print(func(42))

@functype
def func(value):
    return value

test(func)

# Test ctypes.CFUNCTYPE(None
