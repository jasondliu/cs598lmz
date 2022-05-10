import ctypes
# Test ctypes.CField
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: test_cfield.py <headerfile>')
        sys.exit(-1)
    ffi = cffi.FFI()
    ffi.cdef("""
        struct foo {
            ...;
        };
    """)
    ffi.CField("foo", "bar", ctypes.c_int)
    ffi.CField("foo", "baz", ctypes.c_int)
    ffi.CField("foo", "quux", ctypes.c_int)
    ffi.compile(tmpdir=sys.argv[1])
