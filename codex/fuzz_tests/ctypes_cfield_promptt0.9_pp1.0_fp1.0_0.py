import ctypes
# Test ctypes.CField
typeinfo = ctypes.CField(ctypes._bug_fix(ctypes._b_c_long_p), "", 0)
assert ctypes.CField.from_address(ctypes._ptr("", ctypes._c_long_p))._type_ == ctypes.c_long_p
assert ctypes._Field(ctypes._bug_fix(ctypes._b_c_long_p), "", 0)._type_ == ctypes.c_long_p
assert ctypes._Field.from_address(ctypes._ptr("", ctypes._c_long_p))._type_ == ctypes.c_long_p
# Test ctypes.CArgObject.__str__
class cstr(ctypes.c_byte):
    def __str__(self):
        return "cstr"
assert str(ctypes.CArgObject(cstr)) == "cstr"
# Python 3: ctypes.Py_ssize_t is an alias for ctypes.c_ssize_t
try:
    import sys
    assert ctypes.sizeof(ctypes.
