import ctypes
# Test ctypes.CFUNCTYPE is defined
libffi_path = None
if os.path.basename(os.__file__) == "ffi.pyo":
    # Python 3.3+
    libffi_path = os.path.join(os.path.dirname(os.__file__), '_ctypes.cpython-33m.so')
else:
    # Python < 3.3
    libffi_path = os.path.join(os.path.dirname(os.__file__), 'libffi-7-x86_64-linux-gnu.so.1')

if not os.path.exists(libffi_path):
    print("Could not find libffi in {}".format(libffi_path))

ffi = FFI()
libffi = ffi.dlopen(os.path.abspath(libffi_path))
ffi.cdef("void printf(const char *format, ...);")
cfunc = ffi.cast("void (*)(const char *)", libffi.printf)

libc =
