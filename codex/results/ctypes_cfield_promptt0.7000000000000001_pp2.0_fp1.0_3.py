import ctypes
# Test ctypes.CField
def test_CField():
    ffi = FFI()
    ffi.cdef("""
        struct foo {
            int a;
            int b;
        };
    """)
    assert repr(ffi.typeof('struct foo').fields_by_name['a']) == "<CField 'a' of 'struct foo'>"
    assert repr(ffi.typeof('struct foo').fields_by_name['b']) == "<CField 'b' of 'struct foo'>"

def test_sized_array():
    ffi = FFI()
    ffi.cdef("int a[13];")
    assert repr(ffi.typeof("int[13]")) == '<ctypes type \'int[13]\'>'
    assert repr(ffi.typeof("int[13]").elements[0]) == "<ctype 'int'>"
    assert ffi.sizeof(ffi.typeof("int[13]")) == 52
    assert ffi.sizeof(ffi.typeof("int[13]").elements[0]) ==
