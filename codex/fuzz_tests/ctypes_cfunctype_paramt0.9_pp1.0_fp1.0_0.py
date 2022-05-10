import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def pyfunc(x):
    return numpy.exp(x)

pyCTYPE = numpy.ctypeslib.ndpointer(dtype=float)
FRESHFUN_CALL = {float: FUNTYPE(None, pyCTYPE),
                 numpy.number: FUNTYPE(None, pyCTYPE),
                 }

# for numpy versions < 1.4 we need to explicitly cast float arrays to
# double, though numpy.exp() should handle that

numpy_version = [int(v) for v in numpy.__version__.split('.')[:2]]
if tuple(numpy_version) < (1, 4):
    array_type = FUNTYPE(None, ctypes.POINTER(ctypes.c_double))
    FRESHFUN_CALL[numpy.ndarray] = array_type
FRESHFUN_CALL[tuple] = array_type


class TestCtypesExp(unittest.TestCase):
    def do(self, fun
