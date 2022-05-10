import ctypes
# Test ctypes.CFUNCTYPE performance (0.05 secs vs 0.18 secs)
@ctypes.CFUNCTYPE(ctypes.c_int)
def cf(x):
    return x + 2

c = [cf(i) for i in range(1000000)]
print(type(c[0]))

# Test functools.partial performance (0.13 secs vs 0.18 secs)
def pf(x, f):
    return f(x) + 2
pf = functools.partial(pf, f=int)

c = [pf(str(i)) for i in range(1000000)]
print(type(c[0]))

# Test lambda performance (0.26 secs vs 0.18 secs)
lf = lambda x: x + 2
c = [lf(i) for i in range(1000000)]
print(type(c[0]))

# Test function performance (0.18 secs)
def f(x):
    return x + 2
c = [f(i) for i in range(1000000)]

