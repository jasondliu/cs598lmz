import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
</code>
The first one is a bit faster:
<code>In [1]: %timeit s = S(); s.x = 1; s.y = 2
1000000 loops, best of 3: 1.27 us per loop

In [2]: %timeit s = S(); s.x = 1; s.y = 2
1000000 loops, best of 3: 1.3 us per loop
</code>
but the second one is more readable.

