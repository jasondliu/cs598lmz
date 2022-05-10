import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint64)

_get_1 = None
_get_2 = None

def set_library(lib):
    global _get_1, _get_2
    _get_1 = lib.get_1
    _get_2 = lib.get_2

def get_1(arg1):
    return _get_1(arg1)

def get_2(arg1, arg2):
    return _get_2(arg1, arg2)

set_library(ctypes.CDLL("./libarray.so"))
</code>
C-File:
<code>uint64_t get_1(uint64_t arg1[100]) {
    return (arg1[0]);
}

uint64_t get_2(uint64_t arg1, uint64_t arg2[100]) {
    return (arg2[0]);
}
</code>
Python-File:
<code>import libarray
c_array = ctypes.c_uint64 * 100
a = c_array(1, 2
