import ctypes
# Test ctypes.CFUNCTYPE.
if sys.version_info >= (3,):
    func_type=CFUNCTYPE(c_int)
else:
    int_type=c_int()
    func_type=CFUNCTYPE(int_type)

@func_type#@CFUNCTYPE(c_int)
def foofunc():
    return -1

foofunc()
# Test ctypes.c_byte and ctypes.c_ubyte

issubclass(c_byte, c_int8)
issubclass(c_ubyte, c_uint8)

c_byte(0)
c_ubyte(0)
c_byte(0).value
c_ubyte(0).value
c_byte(0xff)
c_ubyte(0xff)
c_byte(0xff).value
c_ubyte(0xff).value

c_byte(0xff).value
c_ubyte(0xff).value
c_byte(0xff).value
c_ubyte(0xff).
