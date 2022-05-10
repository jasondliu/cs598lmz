import ctypes
ctypes.cast(ctypes.pointer(self.mem), ctypes.POINTER(self.TYPE)).contents


def malloc(self, n):
    ### YOUR CODE HERE
    return np.zeros(n, dtype=self.dtype)

def free(self, ptr): pass
def realloc(self, ptr, n):
    ### YOUR CODE HERE
    return np.zeros(n, dtype=self.dtype)

libc.malloc.restype = ctypes.c_void_p
libc.malloc.argtypes = [ctypes.c_size_t]
libc.free.argtypes = [ctypes.c_void_p]
libc.realloc.restype = ctypes.c_void_p
libc.realloc.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

class Pointer:
    def __init__(self, n=None, dtype=np.float32, data=None):
        self.dtype = dtype
        self.n = n
        self
