import weakref

from . import _cffi_backend as _ffi
from . import _ctypes_backend as _cffi_backend_ctypes
from . import _ctypes_common_h as _cffi_common_h
from . import _ctypes_test_h as _cffi_test_h

_ffi.cdef("""
    struct struct_of_array {
        int a[16];
    };
    struct struct_of_structs {
        struct { int a, b; } s[16];
    };
""")

def test_struct_of_array():
    for i in range(16):
        assert _ffi.sizeof("struct struct_of_array") == 16 * _ffi.sizeof("int")
        assert _ffi.offsetof("struct struct_of_array", "a[%d]" % i) == i * _ffi.sizeof("int")

def test_struct_of_structs():
    for i in range(16):
        assert _ffi.sizeof("struct
