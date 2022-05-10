import gc, weakref
from ctypes import *

_lib = CDLL("libc.dylib")
_lib.malloc.restype = c_void_p
_lib.free.argtypes = [c_void_p]

class PythonException(Exception):
    pass

class CObject(object):
    def __init__(self):
        self._ptr = _lib.malloc(c_size_t(1))
        if not self._ptr:
            raise PythonException("Failed to allocate 1 byte")
        self.__weakref__ = weakref.proxy(self)

    def __del__(self):
        _lib.free(self._ptr)
        del self._ptr

def main():
    obj = CObject()
    del obj
    gc.collect()

if __name__ == "__main__":
    main()
</code>
I get the following output:
<code>Exception KeyError: KeyError(-330028576,) in &lt;module 'threading' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib
