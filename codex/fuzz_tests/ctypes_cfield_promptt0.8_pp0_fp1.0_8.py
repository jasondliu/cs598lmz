import ctypes
# Test ctypes.CField
class CTest(ctypes.Structure):
    _fields_ = [('name', ctypes.CString, 12),
                ('value', ctypes.c_double),
                ('somethingelse', ctypes.c_void_p),
                ]

print CTest.name
print CTest.value
print CTest.somethingelse
