import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

def static_getter(T):
    global static_getter_T
    static_getter_T = T
    class C:
        a = staticmethod(lambda: 1)
        b = staticmethod(lambda x: 1)
        c = staticmethod(lambda x, y: 1)
        d = staticmethod(lambda x, y, z: 1)
        e = staticmethod(lambda *x: 1)
        f = staticmethod(lambda **x: 1)
        g = staticmethod(lambda *x, **y: 1)
        h = staticmethod(lambda x, *y, **z: 1)

        def __new__(cls):
            return cls.a
    return C

def test_staticmethods_1(C):
    class C(C):
        a = staticmethod(lambda: 2)
    assert C()() == 2

def test_staticmethods_2(C):
    assert C.a() == 1
    assert C.b(1) == 1
    assert C.c(1, 2) == 1
   
