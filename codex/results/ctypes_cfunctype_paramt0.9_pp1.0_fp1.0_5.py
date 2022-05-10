import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_double )

def wrap( func ):
    'helper to "wrap" a C function into a callback'
    def wrapped_func( x ) :
        x = float( x )
        return float( func(x) )
    return FUNTYPE( wrapped_func )

class Function :
    """
    This class contains a function for use by callbacks.
    """
    def __init__( self, func ) :
        """
        Initializes the function callback.  The callback is used in a very
        specific way by this module.  The callback must take one argument, a
        single number, and return a single number.  The callback is assumed to
        be fast in the sense that you would use a C or Fortran function for it.
        If you need a complex function that would be expensive to evaluate, this
        is not the right thing to use.
        """
        self._func = wrap( func )

    def get_FUNTYPE( self ):
        """
        Return the CFUNCTYPE instance used by this object.
        """
        return self._func



