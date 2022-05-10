import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField._length_
ctypes.CField._type_

dir(ctypes.CField)
dir(ctypes.CField._length_)
dir(ctypes.CField._type_)

# p. 241

import ctypes

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    def __str__(self):
        return 'A(%d, %d)' % (self.x, self.y)
print A._fields_
print A._fields_[0]
print A._fields_[0][1]
print A._fields_[0]._type_
print A._fields_[0]._type_.__name__
print A._fields_[0]._length_
print A().__class__.__name__

# p. 242

import ctypes

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_
