import ctypes
# Test ctypes.CField

class CTest:
    def __init__(self):
        self.a = 5

    def __str__(self):
        return "<CTest a=%d >" % (self.a)

    class _fld1(ctypes._SimpleCData):
        _type_ = "i"
    fld1 = ctypes.CField(_fld1)

    class _fld2(ctypes._SimpleCData):
        _type_ = "i"
    fld2 = ctypes.CField(_fld2)

    def _pack_(self, fmt, init=None):
        if init:
            init = struct.Struct(fmt).unpack(init)[0]
        else:
            fmt = None
            init = 0
        return ctypes.Structure.from_address(id(self), fmt, init)

t = CTest()
print t

x = t._pack_("=ii", "1234")
print x
