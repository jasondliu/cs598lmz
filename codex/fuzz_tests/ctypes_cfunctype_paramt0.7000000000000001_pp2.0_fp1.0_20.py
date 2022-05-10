import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

INTERP = [
    (
        "id",
        lambda x: x,
        FUNTYPE(ctypes.c_double)(lambda x: x),
    ),
    (
        "1-x",
        lambda x: 1-x,
        FUNTYPE(ctypes.c_double)(lambda x: 1-x),
    ),
    (
        "1/(1-x)",
        lambda x: 1/(1-x),
        FUNTYPE(ctypes.c_double)(lambda x: 1/(1-x)),
    ),
    (
        "x*x",
        lambda x: x*x,
        FUNTYPE(ctypes.c_double)(lambda x: x*x),
    ),
    (
        "x*x*x",
        lambda x: x*x*x,
        FUNTYPE(ctypes.c_double)(lambda x: x*x*x),
    ),
    (
        "x*x*x*x",
        lambda x: x*x*x
