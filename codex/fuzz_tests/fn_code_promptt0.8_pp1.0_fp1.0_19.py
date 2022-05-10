fn = lambda: None
# Test fn.__code__, fn.__closure__, fn.__traceback__, fn.__name__

def test_fn_code():
    class C():
        def __init__(self, new_code):
            self.__code__ = new_code
        #del __code__
        def __call__(self):
            pass
    c = C(lambda: None)
    c()
    assert c.__code__ == lambda: None
    raises(TypeError, setattr, c, '__code__', 42)

    c = C(lambda: None)
    f = c.__get__(42)
    assert f.__code__ == lambda: None
    raises(TypeError, setattr, f, '__code__', 42)

def test_fn_closure():
    class C():
        def __init__(self, new_closure):
            self.__closure__ = new_closure
        del __closure__
        def __call__(self):
            pass
    c = C(None)
    raises(AttributeError, "c.__closure__")
    assert
