import ctypes
# Test ctypes.CField:
#   allocates memory and hands it out to the caller
#   the caller can use it, but they can not free it (that is the
#   responsibility of the struct) otherwise we'll get a seg fault
#
# See http://docs.python.org/library/ctypes.html#ctypes.CField

addr = ctypes.CField()
ptr = ctypes.pointer(addr)

addr.p = ctypes.pointer(ctypes.c_int(1))
addr.p.contents.value
ctypes.c_int.from_address(addr.value).value

ptr.contents.p.contents.value
ptr.contents.p.contents.value = 2
ptr.contents.p.contents.value

class Address(ctypes.CField):
    def __init__(self, value=0):
        super(Address, self).__init__(value)
        self.p = ctypes.pointer(ctypes.c_int(1))

    def __getattribute__(self, name):
        try:
            return
