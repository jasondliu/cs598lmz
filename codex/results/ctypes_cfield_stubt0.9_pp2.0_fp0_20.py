import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
# assume that it's really a CField, so the rest is the same
def _CData_set(self, newvalue):
    self.__class__._storage_[id(self)] = newvalue

def _CData_get(self):
    # assume that it's really a CField
    classptr = ctypes.cast(ctypes.pointer(self.__class__._storage_), ctypes.POINTER(ctypes.c_void_p))
    ctype = self.__class__.__name__.replace('_Field_', '')
    fieldptr = ctypes.cast(self, ctypes.POINTER(ctype))
    fieldptr.contents = classptr.contents
    return self
    
CField.__get__ = _CData_get
CField.__set__ = _CData_set

class C1(ctypes.Structure):
    _fields_ = [('f1', S.x),
                ('f2', S.x)]

c1 = C1()

c1.f1 == 0        ## ok
