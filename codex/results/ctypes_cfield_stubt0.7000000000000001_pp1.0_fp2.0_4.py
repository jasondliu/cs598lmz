import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

f = S.x
assert f.__name__ == "x"
assert f.__module__ == "__main__"
assert f.__doc__ == None
assert f.offset == 0
assert f.size == 4
assert f.pack == 1
assert f.type == ctypes.c_int
assert f.index == 0

def _test():
    import sys
    _globals = sys._getframe(1).f_globals

    if "ctypes" in _globals:
        del _globals["ctypes"]
    if "sys" in _globals:
        del _globals["sys"]
    if "S" in _globals:
        del _globals["S"]
    if "f" in _globals:
        del _globals["f"]

import pdb
pdb.set_trace()

_test()
