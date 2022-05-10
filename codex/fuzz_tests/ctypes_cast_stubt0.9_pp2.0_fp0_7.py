import ctypes
ctypes.cast(id(1), ctypes.py_object).value

def test_int_alias():
    def f():
        return True
    assert f() is defined(True)
    @expect(True)
    def g():
        return False
    assert g() is undefined


def test_bool_alias():
    def f():
        return 1
    assert f() is defined(1)
    @expect(1)
    def g():
        return 2
    assert g() is undefined

def test_float_alias():
    def f():
        return 1.5
    assert f() is defined(1.5)
    @expect(1.5)
    def g():
        return 2.5
    assert g() is undefined
