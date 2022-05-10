import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def _to_functor(fun):
    if hasattr(fun, '__call__'):
        return FUNTYPE(fun)
    else:
        return ctypes.cast(fun, FUNTYPE)

#-------------------------------------------------------------------

class Spline(object):
    r"""
    Spline interpolation for Python.

    Based on Matlab's Spline Toolkit, which is based on FORTRAN code
    from F. N. Fritsch and J. Butland, Implementation and data for
    not-a-knot end conditions, Mathematics of Computation, 17 (April
    1963) pp. 272-279.

    Uses third order polynomial segments to interpolate through the
    data in x, y. Requires x to be monotonically increasing.
    """

    def __init__(self, x, y, w=None):
        """
        Build a spline object for (x, y) data.

        If w is not None, use it as the sample weights. If not given,
        use equal weights.
        """
