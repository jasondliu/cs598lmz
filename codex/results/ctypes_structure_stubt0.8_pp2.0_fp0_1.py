import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

class Rename(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('_p', ctypes.POINTER(S)),
                ('c', ctypes.c_char * 10),
                ('d', ctypes.c_int),
                ]

    @property
    def p(self):
        return self._p


def main():
    rn = Rename()
    s = S()
    assert rn.c == (ctypes.c_char * 10)()
    assert rn.d == 0
    assert rn.p is None
    rn.p = s
    assert rn.p[0] == s
    rn.p[0].x = 5
    rn.p.x = 5
    rn.p = None

main()
