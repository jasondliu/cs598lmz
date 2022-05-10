import ctypes
# Test ctypes.CFUNCTYPE conversion.
class CFUNCTYPE(ctypes.CFUNCTYPE):
    pass

# Test ctypes.POINTER conversion.
class POINTER(ctypes.POINTER):
    pass

class CStructure(ctypes.Structure):
    metadata = {'version':"1.1"}
    _fields_ = [('foo', ctypes.c_float),
                ('bar', ctypes.c_float),
                ('baz', ctypes.c_float)]

class Baz:
    metadata = {'version':"1.1"}
    def __init__(self, baz):
        self.baz = baz

class Bar:
    metadata = {'version':"1.1"}
    def __init__(self, bar):
        self.bar = bar

class Foo:
    metadata = {'version':"1.1"}
    def __init__(self, foo):
        self.foo = foo

class DummyFunc(ctypes.CFUNCTYPE):
    pass

def func_convert(value
