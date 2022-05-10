import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field_instance():
    assert isinstance(S.x, ctypes.CField)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test_c_field_instance_2():
    assert isinstance(S.x, ctypes.CField)

def test_c_field_instance_3():
    assert isinstance(S.x, ctypes.CField)

def test_c_field_instance_4():
    assert isinstance(S.x, ctypes.CField)

def test_c_field_instance_5():
    assert isinstance(S.x, ctypes.CField)

def test_c_field_instance_6():
    assert isinstance(S.x, ctypes.CField)

def test_c_field_instance_7():
    assert isinstance(S.x, ctypes.CField)

def test_c_field_instance_8():
    assert isinstance(S.x, ctypes.
