import ctypes
# Test ctypes.CFUNCTYPE
# XXX is this the right way to do this?
CFUNCTYPE1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x + 42

f1 = CFUNCTYPE1(f)
print f1(1)
# Test ctypes.POINTER
class POINTER2(ctypes.POINTER):
    _type_ = ctypes.c_int

i = ctypes.c_int(42)
pi = POINTER2(i)
print pi.contents.value
pi.contents.value += 1
print pi.contents.value
print i.value
# Test ctypes.pointer
i = ctypes.c_int(42)
pi = ctypes.pointer(i)
print pi.contents.value
pi.contents.value += 1
print pi.contents.value
print i.value
# Test ctypes.addressof
i = ctypes.c_int(42)
print ctypes.addressof(i)
print c
