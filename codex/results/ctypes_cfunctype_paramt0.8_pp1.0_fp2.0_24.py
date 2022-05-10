import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

_funs = {}

class Function(object):
    def __init__(self, name=None):
        self._cptr = None
        if name is not None:
            self.restore_predefined(name)

    def __del__(self):
        if self._cptr is not None:
            libc.free(self._cptr)

    def restore_predefined(self, predefined_name):
        self._cptr = ctypes.c_void_p(libc.malloc(ctypes.c_size_t(0).value))
        if self._cptr is None:
            raise MemoryError
        libc.function_restore_predefined(self._cptr, predefined_name.encode('utf-8'))

    def set_coefficients(self, coeffs):
        libc.function_set_coefficients(self._cptr,
                                       (ctypes.c_double * len(coeffs))(*coeffs))

    def __call
