import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunction(ctypes.CFuncPtr):
    _flags_ = 0
    _restype_ = None

    def __init__(self, restype=None, *argtypes):
        self._restype_ = restype
        if argtypes:
            self._flags_ = 1
            self.argtypes = tuple(argtypes)
        ctypes.CFuncPtr.__init__(self)

    def from_address(self, address):
        self._flags_ = S._flags_ & FUNCFLAG_FROM_ADDRESS
        self._ptr = address

    def from_param(self):
        if not self:
            return self
        addr = self._ptr
        if not isinstance(addr, (int, long)):
            addr = ctypes.addressof(self._ptr.contents)
        return addr

CFunctionType = ctypes._CFuncPtr

# We don't have to check the return value of this function, because
# in the worst case the "type" variable won't be initialized and the
# caller will get a NULL pointer back
