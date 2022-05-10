import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@types.coroutine
def f(x):
    yield x

# Start a coroutine
c = f(1)

assert type(c) is types.coroutine

# Create a sequence of coroutines
l = [f(i) for i in range(10)]
t = tuple(l)

assert type(t) is tuple
assert type(t[0]) is types.coroutine
assert t[0].ag_frame.f_code == x.ag_frame.f_code
assert t[0].ag_frame.f_lasti == x.ag_frame.f_lasti

d = {}
for i in l:
    d[i] = i

assert type(d) is dict
assert type(d[l[0]]) is types.coroutine
assert d[l[0]].ag_frame.f_code == l[0].ag_frame.f_code
assert d[l[0]].ag_frame.f_lasti == l[0].ag_frame.f_lasti

# Create class with coroutine
