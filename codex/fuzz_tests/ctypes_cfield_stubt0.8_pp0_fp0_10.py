import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyInt(int):
    pass

def print_ptr(p):
    print "%x" % ctypes.cast(p, ctypes.c_void_p).value

def print_field(st, field, value):
    cvalue = ctypes.cast(ctypes.addressof(value), ctypes.POINTER(ctypes.CField))
    name = field[0]
    old = getattr(st, name)
    print_ptr(old)
    setattr(st, name, cvalue)
    print_ptr(getattr(st, name))
    setattr(st, name, old)
    print_ptr(getattr(st, name))

def test_field(st, field):
    print_field(st, field, 1)
    print_field(st, field, 1L)
    print_field(st, field, MyInt(1))

def test():
    st = S()
    test_field(st, S._fields_[0])

if __name__ == '__main__':
   
