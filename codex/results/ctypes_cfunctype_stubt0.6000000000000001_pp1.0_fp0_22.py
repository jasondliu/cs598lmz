import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'foo'

def test_cfuntype_pyobj():
    assert fun() == 'foo'

class Foo(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

    def __repr__(self):
        return '<Foo: %d>' % self.x

    def __eq__(self, other):
        if not isinstance(other, Foo):
            return False
        return self.x == other.x

@FUNTYPE
def fun_struct():
    return Foo(42)

def test_cfuntype_struct():
    assert fun_struct() == Foo(42)

@FUNTYPE
def fun_struct_ptr():
    return Foo(42)

def test_cfuntype_struct_ptr():
    assert fun_struct_ptr() == Foo(42)

@FUNTYPE
def fun_struct_ref():
    return Foo(42)

def test_cfuntype_struct_ref():
    assert fun_struct_ref() == Foo(42)

@FUN
