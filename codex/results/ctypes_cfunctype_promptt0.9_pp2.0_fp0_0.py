import ctypes
# Test ctypes.CFUNCTYPE()
type(CFUNCTYPE(c_int, c_int))

# Test ctypes.addressof()
c_typeid = c_void_p.in_dll(get_libc(), 'typeid')
c_offsetof = c_typeid.value
print c_typeid.value

# Test "<ctype>.from_address()"
def c_from_address(address):
    """Create a new ctypes instance from the address passed in."""
    try:
        return (address).from_address(address)
    except TypeError:
        pass
    for ctype in (c_short, c_int, c_long, c_longlong, c_ubyte,
                  c_ushort, c_uint, c_ulong, c_ulonglong):
        try:
            return ctype.from_address(address)
        except TypeError:
            pass
    raise TypeError("no g
