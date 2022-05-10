import ctypes
# Test ctypes.CField

class Struct(ctypes.Structure):
    _fields_ = [('a', ctypes.CField),
                ('b', ctypes.CField)]

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.CField),
                ('y', ctypes.CField),
                ('z', ctypes.CField)]

class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.CField),
                ('b', ctypes.CField),
                ('c', ctypes.CField),
                ('d', ctypes.CField),
                ('e', ctypes.CField),
                ('f', ctypes.CField),
                ('g', ctypes.CField),
                ('h', ctypes.CField),
                ('i', ctypes.CField),
                ('j', ctypes.CField),
                ('k', ctypes.CField),
                ('l', ctypes.CField),
                ('m', ctypes.CField),
                ('n', ctypes.CField
