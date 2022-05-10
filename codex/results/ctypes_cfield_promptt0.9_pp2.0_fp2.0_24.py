import ctypes
# Test ctypes.CField declaration
class test(ctypes.Structure):
    _fields = (ctypes.CField("a", ctypes.c_char_p),)

# Test ctypes.CFields declaration
class test(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_char_p),
        ("b", ctypes.c_char_p),
    ]

class test(ctypes.Structure):
    _fields_ = [
        ctypes.CField("a", ctypes.c_char_p),
        ctypes.CField("b", ctypes.c_char_p),
    ]

# Test ctypes.CField* declaration
test._fields_         # type: ignore[attr-defined]
test._fields_a        # type: ignore[attr-defined]
test._fields_b        # type: ignore[attr-defined]
test._fields_d        # type: ignore[attr-defined]

# Test structure initialization
a = test(a=b"hello")
a.a                    # type: ignore[attr-
