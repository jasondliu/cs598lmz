import ctypes
ctypes.cast(0, ctypes.py_object).value

ffi = FFI()

ffi.cdef("""
    struct foo {
        char a;
        int b;
        long c;
        char d;
        ...;
    };
""")

class Test_unaligned_structs(unittest.TestCase):
    def test_structure_packing(self):
        ffi = FFI()
        ffi.cdef("""
            struct foo {
                char a;
                int b;
                long c;
                char d;
                ...;
            };
        """)
        lib = ffi.verify("""
            #include <stddef.h>

            struct foo {
                char a;
                int b;
                long c;
                char d;
            };
        """, ext_package='cffi')
        assert ffi.sizeof(lib.foo) == ffi.sizeof("char") + ffi.sizeof("int") + ffi.sizeof("long") + ffi.sizeof("char
