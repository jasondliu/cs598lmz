import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class INHERITABLE_CFIELD(ctypes.CField, object):
    def heck(self):
        return 'haha'

class S(ctypes.Structure):
    _fields_ = [('x', INHERITABLE_CFIELD)]

s = S()

s.x = 42
s.x += 1
s.x = 5.6 # the result should now be 5

################################################################
#
# Test a Field with _pack_ = True and _pack_ = False

class PackTrue(ctypes.Structure):
    _fields_ = [('x', ctypes.c_ubyte, 2)]
    _pack_ = True

class PackFalse(ctypes.Structure):
    _fields_ = [('x', ctypes.c_ubyte, 2)]
    _pack_ = False

pt = PackTrue()
pf = PackFalse()
pt.x = 5
pf.x = 7

## print hex(ctypes.addressof(pt)), pt.x
## print hex(ctypes.addressof
