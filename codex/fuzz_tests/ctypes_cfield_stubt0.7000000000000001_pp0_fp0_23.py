import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunctionType(BuiltinFunctionType):
    """
    Built-in function type that wraps C library functions.
    """

    def __call__(self, *args, **kwargs):
        # Handle the case of functions that take no arguments.
        if self.args is None:
            args = ()

        # Support for "restype" and "argtypes".
        if not hasattr(self, 'restype'):
            self.restype = ctypes.c_int
        if not hasattr(self, 'argtypes'):
            self.argtypes = ()

        # Convert arguments to ctypes.
        cargs = []
        for i, arg in enumerate(args):
            argtype = self.argtypes[i]
            if isinstance(argtype, ctypes.CField):
                cargs.append(argtype(arg))
            elif isinstance(argtype, ctypes.Array):
                if isinstance(arg, PyObject):
                    arg = PyObjectArray(arg)
                cargs.append(argtype(*arg))
            else:
