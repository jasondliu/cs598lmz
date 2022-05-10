import ctypes
# Test ctypes.CField
class Struct1(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    _anonymous_ = ["b"]
    _fields_ = [("b", ctypes.c_int)]

def test_cfield():
    assert Struct1.a == ctypes.c_int
    assert Struct1.b == ctypes.c_int

# Test ctypes.Structure.__new__
def test_structure_new():
    # Test that we can create an instance of a Structure subclass
    # without _fields_ defined
    class S(ctypes.Structure):
        pass
    S()

# Test ctypes.Union.__new__
def test_union_new():
    # Test that we can create an instance of a Union subclass
    # without _fields_ defined
    class U(ctypes.Union):
        pass
    U()

# Test ctypes.CField.__new__
def test_cfield_new():
    # Test that we can create an instance of a CField subclass
    # without _type_
