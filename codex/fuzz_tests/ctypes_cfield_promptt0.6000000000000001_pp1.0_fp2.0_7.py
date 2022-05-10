import ctypes
# Test ctypes.CField
try:
    class C(ctypes.Structure):
        _fields_ = [("a", ctypes.c_char_p),
                    ("b", ctypes.CField)]
except TypeError:
    pass
else:
    print "CField accepted as a structure field"

# Test that _fields_ is a tuple
try:
    class D(ctypes.Structure):
        _fields_ = ["a", "b"]
except TypeError:
    pass
else:
    print "non-tuple accepted as _fields_"

# Test that the last field is a list
try:
    class E(ctypes.Structure):
        _fields_ = [("a", ctypes.c_char_p),
                    ("b", ctypes.c_char_p, 42)]
except TypeError:
    pass
else:
    print "non-tuple accepted as _fields_"

# Test that the last field is a list
try:
    class F(ctypes.Structure):
        _fields_ = [("a", ctypes.c_char_
