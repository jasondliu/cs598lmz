import ctypes
# Test ctypes.CFUNCTYPE()
CFUNCTYPE = ctypes.CFUNCTYPE
c_int_p = ctypes.POINTER(ctypes.c_int)
buffer_from_ptr = ctypes.pythonapi.PyBuffer_FromReadWriteMemory
buffer_from_ptr.restype = ctypes.py_object
buffer_from_ptr.argtypes = [ctypes.c_void_p, ctypes.c_int]
buffer_type = type(buffer_from_ptr(0, 0))
type_crepr = repr
class Array(object):
    """Implement the buffer protocol on top of c_array.

    There is currently no C-API to create a read/write buffer,
    as PyBuffer_FromReadWriteMemory doesn't even exist yet.

    """
    # all writable buffers need to be aligned to at least this number
    # of bytes
    _ALIGN = ctypes.alignment(ctypes.c_int)

    def __init__(self, arr):
        self.arr = arr
    def __getbuffer__(self, obj, slice=None):

