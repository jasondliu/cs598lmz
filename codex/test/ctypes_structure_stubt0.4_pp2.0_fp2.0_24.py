import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def test_ctypes_struct_class_attribute():
    # Check that the class attribute is the same
    assert S.x is T.x
    assert S.y is T.y
    assert S._fields_ is T._fields_

def test_ctypes_struct_instance_attribute():
    # Check that the instance attribute is the same
    s = S()
    t = T()
    assert s.x is t.x
    assert s.y is t.y
    assert s._fields_ is t._fields_

def test_ctypes_struct_instance_attribute_set():
    # Check that the instance attribute is the same
    s = S()
    t = T()
    s.x = t.x = 42
    assert s.x == t.x
    assert s.x == 42
