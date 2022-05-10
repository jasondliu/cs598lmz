import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
from ..auxiliary.type_conv import TypeConv
from .decorator import decorator

class Cpp(TypeConv):
    """
    Uses ctypes to create a python function from a C++ function.

    The actual call to the C++ function is done with ctypes.
    """

    def __init__(self, name, lib, check=True, dtype=np.double):
        """
        Constructor.
        
        :param name: name of the function
        :param lib: ctypes library that contains the function
        :param check: whether input values should be checked
        :param dtype: data type of the function
        """
        self.name = name
        self.lib = lib
        self.check = check
        self.dtype = dtype

    def __call__(self, f):
        """
        Defines the C++ function to be used.

        :param f: C++ function
        """
        self.f = f
        return self

    def _convert(self
