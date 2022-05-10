import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))

def _get_cfun(name):
    return FUNTYPE(("_" + name).encode("ascii"))

lgamma = _get_cfun("lgamma")
gamma = _get_cfun("gamma")
gammaln = _get_cfun("gammaln")

def lgamma_2(x):
    return lgamma(x)

def gamma_2(x):
    return gamma(x)

def gammaln_2(x):
    return gammaln(x)

def test_indexing():
    for n in range(1, 5):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    a = [0] * n**3
                    a[i * n * n + j * n + k] = 1
                    b = numpy.array(a, dtype=numpy.int32)
                    c = numpy
