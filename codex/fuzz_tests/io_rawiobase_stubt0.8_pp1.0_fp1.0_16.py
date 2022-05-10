import io
class File(io.RawIOBase):
    def __init__(self, h, mode=None):
        self._h = h
        self._mode = mode

    def readinto(self, b):
        assert isinstance(b, bytearray)
        r = ctypes.c_int()
        size = len(b)
        ctypes.pythonapi.PyObject_AsReadBuffer(ctypes.py_object(b),
                                               ctypes.c_void_p(0), ctypes.c_void_p(0),
                                               0, ctypes.c_void_p(0))
        result = ctypes.pythonapi.PyObject_CallMethod(self._h, b"readinto",
                                                      b"iiO", ctypes.byref(r),
                                                      size, ctypes.py_object(b))
        if result == None:
            raise IOError("reading error")
        return r.value

def open(name, mode=""):
    h = ctypes.pythonapi.PyFile_FromString(name.encode(), mode.encode())
    return
