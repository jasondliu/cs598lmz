import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
try:
    fun()
except TypeError:
    pass
else:
    raise Exception("Did not raise TypeError")

# Issue2373
import sys
if sys.maxsize > 2**32:
    def a():
        import sys
        return sys.maxsize
    a()

# Issue2389
if sys.platform.startswith("linux"):
    import ctypes
    libc = ctypes.CDLL(None, use_errno=True)
    libc.getchar()
    libc.getc.errcheck = lambda result, func, arguments: result
    for c in 'defg':
        libc.ungetc(ord(c), 0)
    assert libc.getc() == ord("g")
    assert libc.getc() == ord("f")
    assert libc.getc() == ord("e")
    assert libc.getc() == ord("d")
    assert libc.getc() == ord("a")
    libc.ungetc(ord("b"), 0)
    assert
