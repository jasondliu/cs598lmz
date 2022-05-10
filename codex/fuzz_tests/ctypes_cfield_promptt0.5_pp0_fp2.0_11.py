import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.CField)]

x = X()
x.a = 1
print('x.a =', x.a)

# Test ctypes.CField.from_address
class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.CField)]

y = Y()
y.a = 1
print('y.a =', y.a)

# Test ctypes.CField.from_param
def f(a, b):
    print('a =', a)
    print('b =', b)

f(1, 2)
f(ctypes.CField.from_param(1), ctypes.CField.from_param(2))

# Test ctypes.CField.from_buffer
a = ctypes.create_string_buffer(b'abc')
print('a =', a.raw)
print('a.value =', a.value)

# Test ctypes.CField.from_buffer_copy
b =
