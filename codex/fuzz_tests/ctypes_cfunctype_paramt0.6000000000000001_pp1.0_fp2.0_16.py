import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def test_all():
    c = C()
    assert c.get_func()(2.0) == 4.0
    c.set_func(FUNTYPE(lambda x: x*2.0))
    assert c.get_func()(2.0) == 4.0
    c.set_func(None)
    assert c.get_func()(2.0) == 4.0
    c.set_func(lambda x: x)
    assert c.get_func()(2.0) == 2.0
    c.set_func(c.get_func())
    assert c.get_func()(2.0) == 2.0

if __name__ == '__main__':
    test_all()
