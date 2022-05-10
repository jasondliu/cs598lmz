import ctypes
# Test ctypes.CFUNCTYPE without param flags (where possible)

from ctypes import *

def test(tp):
    proto = CFUNCTYPE(tp)
    v = proto(lambda x: x)
    res = v(42)
    print(tp, v, res)
    assert res == 42

