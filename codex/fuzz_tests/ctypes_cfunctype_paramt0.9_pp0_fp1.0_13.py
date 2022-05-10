import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def as_function(fd, functype=FUNTYPE):
    """Use this to convert a file descriptor to a ctypes function. It
    should return a CFUNCTYPE object that can be called.

    It's guaranteed to work on Linux, but will probably not work on
    Windows or Mac OS X.

    Here's an example that accepts a filename, reads the first function
    from that file, and prints a hello message::

      fd = open("/lib/libc.so.6", "rb")
      hello = ctypes.CFUNCTYPE(None)(as_function(fd))
      hello()
    """
    return functype(ctypes.pythonapi.PyCObject_AsVoidPtr.restype(functype))(fd)
