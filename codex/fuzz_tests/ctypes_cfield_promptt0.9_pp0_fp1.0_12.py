import ctypes
# Test ctypes.CField variables
class PFO_FO(object):
    size = 10
class PFO_FO2(object):
    size = 20

class PFO_FO3(ctypes.CField.type):
    _fields_ = [("foo", ctypes.CField(PFO_FO)),
                ("foo2", ctypes.CField(PFO_FO2))]
pfo = PFO_FO3()
pfo.foo = PFO_FO()
pfo.foo2 = PFO_FO2()

ctypes.cast(ctypes.addressof(pfo), ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int)))


class CField(object):
    __metaclass__ = ctypes.CFieldMeta

class X(ctypes.CClass.type):
    _fields_ = [("x", CField)]
    
class Y(X):
    _fields_ = [("y", CField)]

o = Y()
assert Y.x.offset == ctypes.Structure.x.offset
print(ct
