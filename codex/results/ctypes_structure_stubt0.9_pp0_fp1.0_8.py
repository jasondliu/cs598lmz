import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

@jit(nopython=True, boundscheck=False, inline="always")
def nontrivial_init():
    s = S()
    s.x = 1
    s.y = 2
    r = 3.0
    r *= s.x
    return r

def test_non_trivial_init():
    assert nontrivial_init() == 3.0
