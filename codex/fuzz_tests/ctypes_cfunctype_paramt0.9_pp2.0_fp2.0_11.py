import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_int, ctypes.c_int, ctypes.c_int )

# ---------------------------------------
def create_wrap_func(func):
    """Creates a callable wrapper that converts numpy arrays to ctypes pointers
    """
    def wrap_gof_func(p, hx, hy, n, ndim, fjac, ldfjac, x, fvec, ldfvec, xp, 
        fvecp, userbreak, iflag ):
        # Wrap function
        p_array = (ctypes.c_double * n).from_address( p )
        hx_array = (ctypes.c_double * 2).from_address( hx )
        hy_array = (ctypes.c_double * 2).from_address( hy )
        x_array = (ctypes.c_double * n).from_address( x )
        fvec_array = (ctypes.c_double * n).from_address( fvec )
        p_array = numpy.ctypeslib.as_array( p_
