import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
f = CMPFUNC(func)
f

try:
    f(1, 2)
except Exception as e:
    print(e)

f(ctypes.pointer(ctypes.c_int(1)), ctypes.pointer(ctypes.c_int(2)))

# Test ctypes.byref
def func(i, j, k):
    if i.value < j.value:
        i, j = j, i
    if j.value < k.value:
        j, k = k, j
    if i.value < j.value:
        i, j = j, i
    return i.value, j.value, k.value

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes
