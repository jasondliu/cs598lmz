import ctypes
# Test ctypes.CField
#
# XXX Alternative: use ctypes.c_int.in_dll

import ctypes.test.test_cfield

try:
    ctypes.c_int.in_dll(ctypes.test.test_cfield, "i")
except OSError:
    raise ctypes.test.test_cfield.SkipTest("libctypes_test_cfield not found")

# Load the library, and retrieve the address of the int in the library
i = ctypes.c_int.in_dll(ctypes.test.test_cfield, "i")

# Create a new int and make it mirror the library's int
j = ctypes.c_int()
ctypes.pointer(j)[0] = i.value
i.value += 1

assert j.value == ctypes.c_int.in_dll(ctypes.test.test_cfield, "i").value - 1
