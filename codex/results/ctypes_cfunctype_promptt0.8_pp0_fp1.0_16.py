import ctypes
# Test ctypes.CFUNCTYPE and ctypes.byref

try:
    ffi
except NameError:
    import sys
    if sys.platform == 'win32':
        extra_compile_args = ['-m32']
        extra_link_args = ['-m32']
    else:
        extra_compile_args = ['-fPIC', '-O2']
        extra_link_args = []
    ffi = FFI()
ffi.cdef("int ffi_test_callback_A(int (*cb)(char *, ...));")
C = ffi.verify("""
int ffi_test_callback_A(int (*cb)(char *, ...))
{
    char *s = "foo";
    return cb(s);
}
""",
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

if sys.platform == 'win32':
    def do_something(s):
        return ord(s[0])
elif sys.platform in ('darwin',
