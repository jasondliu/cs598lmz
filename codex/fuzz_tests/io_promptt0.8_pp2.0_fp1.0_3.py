import io
# Test io.RawIOBase subclass
import _io
_io.FileIO = type('FileIO', (_io.RawIOBase,), {'write': None})
# Test old-style class
class OldStyleClass:
    pass
# Test new-style class
class NewStyleClass(object):
    pass
import _testcapi
# Test _testcapi.with_tp_del
class C(_testcapi.with_tp_del):
    pass

class D:
    pass
C.__del__ = D.__del__

class E(_testcapi.with_tp_del):
    pass

# Test __del__ methods
class F(object):
    def __del__(self): pass

class G:
    def __del__(self): pass

class H(F, G):
    pass

# Test tuple subclasses
class tuple2(tuple):
    pass

class tuple3(tuple):
    def __new__(cls, *args):
        return tuple.__new__(tuple, args)

class tuple4(tuple):
   
