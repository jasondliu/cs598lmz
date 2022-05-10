import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_uint,
    ctypes.c_void_p)

class SPSA(object):

    def __init__(self, 
            n, 
            f, 
            p=0.6, 
            a=1, 
            c=0.1, 
            alpha=0.602,
            gamma=0.101, 
            max_iter=1000, 
            callback=None, 
            gtol=1E-10,
            save_x=True):
        self.save_x = save_x
        self.gtol = gtol
        self.callback = callback
        self.max_iter = max_iter
        self.n = n
        self.f = FUNTYPE(f)
        self.p = p
        self.a = a
        self.c = c
        self.alpha = alpha
        self.gam
