import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
@cpython_api([ctypes.CField], lltype.Signed, error=-1)
def PyCField_AsLong(space, w_obj):
    """
    PyCField_AsLong is deprecated and should not be used in new code.
    Use the Python-level x.value attribute instead.
    """
    return PyInt_AsLong(space, w_obj.value)
