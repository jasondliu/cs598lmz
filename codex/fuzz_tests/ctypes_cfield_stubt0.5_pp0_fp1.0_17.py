import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldPointer = type(S._fields_[0])
ctypes.CFieldArray = type(S._fields_[0][1])
ctypes.CField_p = type(S._fields_[0][0])

class S1(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]


# the following test checks that the types of the _fields_
# elements are not changed by the accesses:
def test1():
    f = S._fields_[0]
    assert type(f) is ctypes.CFieldPointer
    assert type(f[0]) is ctypes.CField_p
    assert type(f[1]) is ctypes.CFieldArray
    assert type(f[1][0]) is ctypes.CField

    f = S
