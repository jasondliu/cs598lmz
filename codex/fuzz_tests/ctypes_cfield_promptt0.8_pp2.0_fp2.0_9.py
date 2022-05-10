import ctypes
# Test ctypes.CField
libc = ctypes.CDLL(ctypes.util.find_library("c"))

# string_at() is not available during bootstrap,
# use cast() instead.
def cstr(ptr, maxlen):
    length = 0
    while ptr[length] and length < maxlen:
        length += 1
    return ctypes.cast(ptr, ctypes.c_char_p).value[:length]

class TestCField(unittest.TestCase):
    def test_get_type(self):
        getname = libc.getpwuid
        getname.argtypes = ctypes.c_int,
        getname.restype = ctypes.POINTER(ctypes.c_char * 256)

        self.assertEqual(getname(0).contents.__class__, ctypes.c_char * 256)
        self.assertEqual(getname(0).contents.__class__(getname(0).contents),
                          cstr(getname(0).contents, 256))

    def test_discarded_att
