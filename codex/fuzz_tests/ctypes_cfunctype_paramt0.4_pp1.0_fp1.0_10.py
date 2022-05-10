import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def _make_func(func):
    """
    Return a ctypes function pointer for the given function.
    """
    return FUNTYPE(func)

def _make_func_ptr(func):
    """
    Return a ctypes pointer to a function pointer for the given function.
    """
    return ctypes.POINTER(FUNTYPE)(_make_func(func))

def _make_func_ptr_ptr(func):
    """
    Return a ctypes pointer to a pointer to a function pointer for the given
    function.
    """
    return ctypes.POINTER(ctypes.POINTER(FUNTYPE))(_make_func_ptr(func))

class _TestCase(unittest.TestCase):
    """
    Base class for test cases using the C API.
    """

    @classmethod
    def setUpClass(cls):
        """
        Load the C API.
        """
        cls.lib = ctypes.cdll.LoadLibrary(os.path.join(os
