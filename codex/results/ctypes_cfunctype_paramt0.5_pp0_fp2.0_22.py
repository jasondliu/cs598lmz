import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def wrap_function(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

class Image(object):
    """Wrapper for C struct Image"""
    def __init__(self, w, h, data=None):
        """Create an image of width w and height h"""
        self.w = w
        self.h = h
        if data is None:
            self.data = w*h*ctypes.c_double()
        else:
            self.data = data
        self.pixels = np.ctypeslib.as_array(self.data, (h, w))

    def as_array(self):
        """Return a numpy array of the image"""
        return self.pixels

    def as_image(self):
        """Return a Python Imaging Library image of the image"""
        return Image.fromarray(self.as
