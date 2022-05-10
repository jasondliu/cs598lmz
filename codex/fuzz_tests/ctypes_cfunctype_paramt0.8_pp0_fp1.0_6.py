import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

# These names are specified by Python for inclusion in the PyMethodDef type.
_ml_meth_name = '_ml_meth'
_ml_meth_doc = '_ml_meth_doc'


def _make_ml_fun(fun, nargs):
    """
    Return a ctypes function for fun that takes nargs arguments.
    """
    c_fun = FUNTYPE(fun)
    c_args = (ctypes.c_int,) * nargs
    return c_fun(*c_args)


class _PyMethodDef(ctypes.Structure):
    """
    Structure used to define a Python C method object.
    This is the type of the ml_meth field in PyMethodDef.
    """
    _fields_ = [('ml_name', ctypes.c_char_p),
                ('ml_meth', FUNTYPE),
                ('ml_flags', ctypes.c_int),
                ('ml_doc', ctypes.c_char_p)]



