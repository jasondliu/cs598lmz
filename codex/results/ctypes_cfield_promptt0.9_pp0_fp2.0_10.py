import ctypes
# Test ctypes.CField
import ctypes.util
unix = (os.name == 'posix') and ctypes.util.find_library('c')
if unix:
    libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Compare ctypes.addressof() with ctypes.c_void_p.from_address()

if unix:
    libc.printf(b'printf works!')
    print(libc.time(0))
    libc.printf(b'printf works!')
    print(libc.system(b"echo 'echo works!'"))

# Test libffi support
#if unix:
#    from ctypes_configure.libffi_msvc import ffi, lib
#    lib.printf(b'printf works!')
#    print(lib.time(0))
#    lib.system(b"echo 'echo works!'")

setup_file =  "cmodule.c"
reffile =  "cmodule.py"

self.compile(["cmodule.c"],
