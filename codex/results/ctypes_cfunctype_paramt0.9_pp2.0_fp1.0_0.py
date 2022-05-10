import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)
TEST_OPTIONS = {
    'cvxopt_for_test' : False
}
def square(x):
    return x * x

def f(x):
    return square(x[0] * x[3] * (x[0] + x[1] + x[2]) + x[2])

def df(x):
    return numpy.array([
        2.0 * x[0] * x[3] * (x[0] + x[1] + x[2]) + x[0] * x[3] + x[3] * (x[0] + x[1] + x[2]) + 2.0 * x[2],
        x[3] * (x[0] + x[1] + x[2]),
        2.0 * x[0] * x[3] * (x[0] + x[1] + x[2]) + x[0] * x[3] + x[3] * (x[0] + x[1] + x[2])
