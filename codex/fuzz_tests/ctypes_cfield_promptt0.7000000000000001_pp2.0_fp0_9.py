import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [('a', ctypes.CField)]

class B(ctypes.Structure):
    _fields_ = [('a', ctypes.CField),
                ('b', ctypes.CField)]

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.CField),
                ('b', ctypes.CField),
                ('c', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.CField * 2)]

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.CField * 2),
                ('b', ctypes.CField * 2)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.CField * 2),
                ('b', ctypes.CField * 2),
                ('c', ctypes.CField * 2)]

class G(ctypes.Structure):
    _fields_ =
