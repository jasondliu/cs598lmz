import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

try:
    import _ctypes
except ImportError:
    pass
else:
    # Test the _ctypes module
    print 'Testing _ctypes'
    _ctypes_test.exception_test()
    _ctypes_test.funcptr_test()

if sys.platform == "win32":
    from _ctypes import LoadLibrary, FreeLibrary, GetProcAddress

    kernel32 = LoadLibrary("kernel32")
    # XXX The following line is a workaround for a bug in Mingw32's
    # implemenation of GetProcAddress(): It doesn't add an underscore
    # to the function name, like msvcrt's GetProcAddress() does.
    # This is fixed in CVS.
    GetStdHandle = GetProcAddress(kernel32, "GetStdHandle")
    assert GetStdHandle, "GetStdHandle not found"
    FreeLibrary(kernel32)

print 'Testing ctypes'

# A simple callback function
CALLBACK = CFUNCTYPE(c_int, c
