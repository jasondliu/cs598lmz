import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
C_FUN = FUNTYPE(lambda n, a: n + a)

python_fn = lambda n, a: n + a

print([python_fn(*args) for args in zip(range(5), repeat(10))])
# [10, 11, 12, 13, 14]

print([C_FUN(*args) for args in zip(range(5), repeat(10))])
# [10, 11, 12, 13, 14]
</code>

