import ctypes
# Test ctypes.CField implementation
class SomeStruct(ctypes.Structure):
    _field_ = [("a", ctypes.c_int),
               (None, ctypes.c_int),
               (None, ctypes.c_int),
               ("b", ctypes.c_int),
              ]
    def __init__(self, *args):
        ctypes.Structure.__init__(self, *args)
        self.a = 42
        self.b = 43

class SomeUnion(ctypes.Union):
    _field_ = [("a", ctypes.c_int),
               (None, ctypes.c_int),
               (None, ctypes.c_int),
               ("b", ctypes.c_int),
              ]
    def __init__(self, *args):
        ctypes.Union.__init__(self, *args)
        self.a = 42
        self.b = 43

# The test for None should fail:
try:
    class SomeStruct2(ctypes.Structure):
        _fields_ = [("a",
