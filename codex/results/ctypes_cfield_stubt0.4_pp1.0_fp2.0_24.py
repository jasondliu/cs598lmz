import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__str__ = lambda self: self.name

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)
ctypes.CStructure.__str__ = lambda self: '<%s>' % self.__name__

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(D)
ctypes.CUnion.__str__ = lambda self: '<%s>' % self.__name__

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CPointer = type(ctypes.pointer(E()))
ctypes.CPointer.__str__ = lambda self: '*%s' % self._type_

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes
