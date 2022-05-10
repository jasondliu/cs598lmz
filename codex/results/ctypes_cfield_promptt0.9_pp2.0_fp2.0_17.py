import ctypes
# Test ctypes.CField.__repr__()
# http://bugs.python.org/issue13451
import test
test.support.requires('ctypes')

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int)]
cfield_test = ctypes.CField(X._fields_[0])
if ctypes.__version__ < "1.1.0":
    expected = "CField(_CData('a', 'i'), <field 'a' of 'X' structures>)"
else:
    expected = "<CField 'a' of type 'i'>"
print(repr(cfield_test), expected)
