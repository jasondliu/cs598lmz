import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.CField):
    def _check_retval_(self, result):
        print 'something'
        return result.value

class D(S):
    _fields_=S._fields_+ [("y", C)]


if __name__  == '__main__':
    d=D()
    d.y
