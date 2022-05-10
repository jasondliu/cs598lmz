import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(S):
    _fields_ = [('y', ctypes.c_int)]

def test_cfield_subclass():
    assert isinstance(D.x, ctypes.CField)
    assert isinstance(D.y, ctypes.CField)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D2(S2):
    _fields_ = [('y', ctypes.c_int)]

def test_cfield_subclass_after():
    assert isinstance(D2.x, ctypes.CField)
    assert isinstance(D2.y, ctypes.CField)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

S3._fields_ = [('y', ctypes.c_int)]

def test_cfield_subclass_after2():
    assert isinstance(S3.x, ctypes.CField)
    assert isinstance(S
