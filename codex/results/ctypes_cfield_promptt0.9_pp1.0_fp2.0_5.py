import ctypes
# Test ctypes.CField, ctypes.CField.__get__(), and ctypes.CField.__set__().


class C(ctypes.Structure):
    _fields_ = [('value', ctypes.c_int)]
    _anonymous_ = []


class CBase(ctypes.Union):
    _anonymous_ = [('c', C)]


class CSub(CBase):
    _fields_ = [('c', C), ('x', ctypes.c_char)]
    _anonymous_ = [('c', C)]
    _pack_ = 1


def CheckCField(t, fld):
    print(t, fld)
    b = t()
    f = getattr(b, fld)
    v0 = ctypes.c_int(0x12345678)
    print(type(f), f.offset, f.size)
    print('b.{}.offset: {}'.format(fld, getattr(getattr(b, fld), 'offset')))
    print('b.{}.size: {}'.format(fld, get
