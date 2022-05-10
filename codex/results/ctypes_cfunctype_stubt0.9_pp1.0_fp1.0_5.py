import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def f():
    return fun

for i in range(500):
    f()
    if i == 490:
        PROFILER.f = f

fun.__del_
def toto():
    return f()()()()()()()()()()()()()()()()()()()()()()()()()

s = PROFILER.f()
assert 42 == PROFILER._line_number(s)
print "__name__", repr(fun.__name__)
assert '<trampoline closure>' in repr(fun.__name__)
#assert 'fun' in repr(fun.__code__.co_filename) # XXX bug in PROFILER, not_defined
assert fun.__doc__ is None
assert fun.__module__ == '__main__'

# check that this doesn't crash
import ctypes
import sys
def crash():
    return ctypes.pythonapi.PyTuple_Pack(1, id(sys))

crash()
