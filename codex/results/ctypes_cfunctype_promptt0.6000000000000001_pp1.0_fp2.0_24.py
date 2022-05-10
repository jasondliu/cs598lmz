import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

@_ctypes_test.CFuncPtr
def func(i):
    return i * 2

print(func(2))

@_ctypes_test.CFuncPtr
def func2(i, j, k):
    return i * 2 + j * 3 + k * 4

print(func2(1, 2, 3))


@_ctypes_test.CFuncPtr
def func3(i, j, k, l):
    return i * 2 + j * 3 + k * 4 + l * 5

print(func3(1, 2, 3, 4))


@_ctypes_test.CFuncPtr
def func4(i, j, k, l, m):
    return i * 2 + j * 3 + k * 4 + l * 5 + m * 5

print(func4(1, 2, 3, 4, 5))

@_ctypes_test.CFuncPtr
def func5(i, j, k, l, m, n):
    return i * 2 + j * 3 + k *
