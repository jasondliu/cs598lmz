import ctypes
# Test ctypes.CField
assert ctypes.CField == ctypes._CData

import ctypes.wintypes
assert ctypes.wintypes.LPSTR == ctypes.POINTER(ctypes.c_char)

# Test ctypes.sizeof(None)
assert ctypes.sizeof(None) == 0

# Test pointer arithmetic
import operator
for tp in (ctypes.c_byte, ctypes.c_ubyte, ctypes.c_short, ctypes.c_ushort,
           ctypes.c_int, ctypes.c_uint, ctypes.c_long, ctypes.c_ulong,
           ctypes.c_longlong, ctypes.c_ulonglong):
    for op in (operator.add, operator.sub):
        ptr = tp.from_address(123)
        ptr2 = op(ptr, 1)
        assert ptr2.value == op(ptr.value, 1)
        assert ptr2.value == tp.from_address(op(ptr.value, 1)).value
        assert ptr2.value == op(tp
