import ctypes
# Test ctypes.CField_test0_t, this declares a simple structure type, with
# subtypes of all the basic types supported by ctypes, and a pointer.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_long),
                ("c", ctypes.c_double),
                ("d", ctypes.c_char),
                ("e", ctypes.c_wchar),
                ("f", ctypes.c_byte),
                ("g", ctypes.c_ubyte),
                ("h", ctypes.c_short),
                ("i", ctypes.c_ushort),
                ("j", ctypes.c_uint),
                ("k", ctypes.c_longlong),
                ("l", ctypes.c_ulonglong),
                ("m", ctypes.c_void_p)]

if __name__ == "__main__":
    import test.test_ctypes
    test.test_ctypes.run_unittest(__name__)
