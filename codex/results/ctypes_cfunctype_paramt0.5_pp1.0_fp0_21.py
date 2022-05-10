import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

def callback(a):
    print('callback:', a)
    return a

CALLBACK = FUNTYPE(callback)

lib.callback(CALLBACK)

print(lib.get_a())

lib.set_a(5)

print(lib.get_a())

a = A()
a.a = 10

lib.set_a_struct(a)

print(lib.get_a())

lib.set_a_ref(ctypes.byref(a))

print(lib.get_a())

print(lib.get_a_struct())

print(lib.get_a_ref())

lib.set_a_ptr(ctypes.pointer(a))

print(lib.get_a())

print(lib.get_a_struct())

print(lib.get_a_ref())

print(lib
