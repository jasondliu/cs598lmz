import ctypes
# Test ctypes.CField()
import ctypes.test
print(ctypes.CField)

# Test ctypes.c_char_p.in_dll()
print(ctypes.c_char_p.in_dll(ctypes.CDLL(None), 'stderr'))

# Test ctypes.util.find_msvcrt()
print(ctypes.util.find_msvcrt())

import _ctypes_test

# test pythonapi
ctypes.pythonapi.Py_InitModule4.restype = ctypes.py_object
ctypes.pythonapi.Py_InitModule4.argtypes = [ctypes.c_char_p, ctypes.py_object, ctypes.c_char_p, ctypes.py_object, ctypes.c_int]

module = ctypes.pythonapi.Py_InitModule4(_ctypes_test.__name__.encode('ascii'), _ctypes_test._test_functions, b"docstring", None, 1013)
assert module is _ctypes_test

# check that type and instance
