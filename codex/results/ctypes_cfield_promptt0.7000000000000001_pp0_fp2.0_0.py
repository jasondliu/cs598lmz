import ctypes
# Test ctypes.CField

CFieldTest = ctypes.Structure("CFieldTest",
                              ([("x", ctypes.c_int),
                                ("y", ctypes.c_int)],
                               {"i": ctypes.c_int,
                                "j": ctypes.c_int,
                                "s": ctypes.c_char_p}),
                              (ctypes.CFUNCTYPE(ctypes.c_int),))

class CFieldTest(CFieldTest):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.i = 0
        self.j = 0
        self.s = "hello world"
        self._as_parameter_ = self

# test __getitem__
cp = ctypes.POINTER(CFieldTest)()
assert type(cp) is ctypes.POINTER(CFieldTest)
assert cp[0].x == 0
assert cp[0].y == 0
assert cp[0].i == 0
assert cp[0].j == 0
assert cp[0
