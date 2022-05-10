import ctypes
# Test ctypes.CField()
import ctypes
class X(ctypes.Structure):
    _fields_ = [
        ("one", ctypes.c_int),
        ("two", ctypes.c_int),
        ("three", ctypes.c_int),
        ("four", ctypes.c_int),
        ("five", ctypes.c_int),
    ]

    def __repr__(self):
        return "X(%s)" % ", ".join([
            repr(getattr(self, name)) for name, _ in self._fields_
        ])

print(X())                            #X(0, 0, 0, 0, 0)

print(X.one)                          #__main__.c_long

X.one = 1 # This is OK

print(X())                            #X(1, 0, 0, 0, 0)

X.one = "" # This used to raise SystemError, now raises TypeError

print(X())                            #X(0, 0, 0, 0, 0)

# Test struct module
#
# See also test
