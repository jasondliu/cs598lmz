import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64()
    y = ctypes.c_int64()

class A(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int64()),
                ("y", ctypes.c_int64())
               ]

s = S()
a = A()

# A is faster than S, but still slow
print timeit.timeit("s.x = 0; s.y = 0", setup="from __main__ import s", number=10000000)
print timeit.timeit("a.x = 0; a.y = 0", setup="from __main__ import a", number=10000000)

# using a list is faster than using a tuple
print timeit.timeit("s.x = 0; s.y = 0", setup="from __main__ import s", number=10000000)
print timeit.timeit("a.x = 0; a.y = 0", setup="from __main__ import a", number=10000000)
</code>
Output:
<code>2.82963109398
