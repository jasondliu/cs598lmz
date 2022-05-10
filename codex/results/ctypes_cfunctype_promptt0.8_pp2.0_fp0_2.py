import ctypes
# Test ctypes.CFUNCTYPE, CFUNCTYPE(None, ctypes.c_int)
class X(ctypes.Structure):
    pass
x = ctypes.c_int()
X._fields_ = [('f0', ctypes.CFUNCTYPE(None, ctypes.c_int)),
              ('f1', ctypes.CFUNCTYPE(None, ctypes.c_int))]

print X.from_address(id(X())).f0(x)
print X.from_address(id(X())).f1(x)
print X.from_address(id(X())).f0(x)
print X.from_address(id(X())).f1(x)
X.from_address(id(X())).f0
print X.from_address(id(X())).f0(x)
print X.from_address(id(X())).f1(x)

class CFunctionTypeTestCase(unittest.TestCase):
    def test_argtypes(self):
        c_sin = ctypes.CDLL(ct
