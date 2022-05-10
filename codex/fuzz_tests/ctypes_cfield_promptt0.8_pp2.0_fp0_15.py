import ctypes
# Test ctypes.CField.from_address
import ctypes
class SimpleType(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    
class ComplexType(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("next", ctypes.POINTER(ComplexType))]
    
def sanity_check(value):
    obj = SimpleType.from_address(value)
    obj.x = 42
    return obj.x

def chained_pointer_sanity_check(value):
    obj = ComplexType.from_address(value)
    obj.x = 42
    next = obj.next.contents
    next.x = 37
    return obj.x + next.x

def test_from_address():
    assert sanity_check(id(sanity_check)) is 42
    assert chained_pointer_sanity_check(id(chained_pointer_sanity_check)) is 79
    raises(TypeError, "SimpleType.from_address(None)")
    raises(TypeError, "
