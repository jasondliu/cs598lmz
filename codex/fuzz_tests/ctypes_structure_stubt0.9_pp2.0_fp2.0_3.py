import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def g(arg):
    return ctypes.cast(arg, ctypes.POINTER(S))[0]

def f(arg):
    return ctypes.cast(arg, ctypes.POINTER(S))

def test_f():
    result = f(0)
    assert not result
    result2 = f(0)
    assert not result2
    assert result == result2
    x = S()
    result3 = f(x)
    assert result3
    assert not f(0xffffffff)[0]
    raises(TypeError, f, "hello")
    raises(TypeError, f, u"hello")
    raises(TypeError, f, f)
    raises(TypeError, f, 0.0)

    s = S()
    s.x = 3

    f1 = f(s)

    assert f1[0].x == 3
    f1[0].x = 6
    assert f1[0].x == 6
    assert s.x == 6


def test_g():
    result
