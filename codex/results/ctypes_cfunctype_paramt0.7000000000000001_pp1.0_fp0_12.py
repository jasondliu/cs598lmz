import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def nop(x):
    return x

# Free lists.
_POOL = []
_SPARSEARRAY_POOL = []
_DENSEARRAY_POOL = []
_MATRIX_POOL = []
_SPARSEMATRIX_POOL = []

def get_pool(n):
    if n < 100000:
        return _POOL
    elif n < 10000000:
        return _SPARSEARRAY_POOL
    elif n < 100000000:
        return _DENSEARRAY_POOL
    elif n < 1000000000:
        return _MATRIX_POOL
    else:
        return _SPARSEMATRIX_POOL

# return the new size of the pool
def grow_pool(pool, size):
    new_size = len(pool)
    while new_size < size:
        new_size *= 3
    pool += [None] * (new_size - len(pool))
    return new_size

# Returns a free memory block of at least size n.
