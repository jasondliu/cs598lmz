import ctypes
# Test ctypes.CField.from_address
import ctypes
class X(ctypes.Union):
    _fields_ = [
        ('p1', ctypes.c_char),
        ('p2', ctypes.c_int)
        ]
myunion = X()
myunion.p2 = 2
assert ctypes.c_int.from_address(ctypes.addressof(myunion)) == myunion.p2
assert ctypes.addressof(X.p1.from_address(ctypes.addressof(myunion))) == ctypes.addressof(myunion.p1)
assert ctypes.addressof(X.p2.from_address(ctypes.addressof(myunion))) == ctypes.addressof(myunion.p2)
class Y:
    pass
myobj = Y()
assert ctypes.c_void_p.from_address(id(myobj)) == id(myobj)

def CustomFieldFromAddressType(obj, type=None):
    return obj

def CustomFieldFromAddress(typ, address):
    return typ.from
