import ctypes
ctypes.cast(defs, ctypes.py_object).value
</code>
It is not recommended, but it is possible and doesn't need unstable API in Cython.
However, as I mention above, I don't think this is a good idea, because I don't know whether the patch <code>&lt;cdef extern from *&gt;</code> that Cython did to support <code>&lt;*&gt;</code> will backport to Cython 0.27.x.

