import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def cfunc(pyfunc):
    cfunc = FUNTYPE(pyfunc)
    return cfunc


from __future__ import division, print_function, absolute_import
from numba import njit, prange

numba_divmod = njit(cfunc(divmod_typed), nogil=True, parallel=False)
</code>
The Cython version:
<code>%%cython -a
#cython: linetrace=True
cimport cython
from libc.stdint cimport int64_t

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef int64_t [:] cython_divmod(double *n):
    cdef:
        Py_ssize_t i
        double n_
        long q_
        long r_
        int64_t [:] divmod_ = &lt;int64_t [: 2]&gt
