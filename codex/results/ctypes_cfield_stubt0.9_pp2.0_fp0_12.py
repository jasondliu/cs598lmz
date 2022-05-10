import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [(None, ctypes.c_int)]

def repr_CField(self):
    '''CField.__repr__() helper function'''
    s = "CField(%s)" % self.fieldname
    if self._cf_type_ is not None:
        s = "(%s)," % (self._cf_type_,) + s
    else:
        s = "ctypes.CFuncPtr," + s
    return s

CField = type(C._fields_[0])
CField(C._fields_[0]).__repr__ = repr_CField

class TEST(ctypes.Structure):
    _fields_ = [('first', ctypes.c_int),
                ('second', ctypes.c_int),
                ('third', ctypes.c_int),
                ('accessor', ctypes.c_int)]

def repr_Field(self):
    s = "("
    if self.name != None:
        s = self.name + "
