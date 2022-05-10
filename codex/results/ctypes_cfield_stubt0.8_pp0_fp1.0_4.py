import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@pytest.fixture
def Field(self):
    return ctypes.CField

class TestCField(FieldsTests):
    pass
