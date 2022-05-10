import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float)
    ]

class Y(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int),
                ('x', ctypes.CField)]

class Z(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int),
                ('x', ctypes.CField, 0)]

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.CField, 1)]

# Test ctypes.CField with non-Structure type

class B(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.CField, 1, ctypes.c_float),
                ('z', ctypes.c_int)]

# Test ctypes.CField with non-Structure type
