fn = lambda: None
# Test fn.__code__
fn.__code__ = bytecode
# Test fn.__closure__
fn.__closure__ = closure
# Test fn.__dict__
fn.__dict__ = dict
# Test fn.__name__
fn.__name__ = "__name__"
# Test fn.__qualname__
fn.__qualname__ = "__qualname__"
# Test fn.__doc__
fn.__doc__ = "__doc__"
# Test fn.__module__
fn.__module__ = "__module__"
# Test fn.__defaults__
fn.__defaults__ = ()
# Test fn.__kwdefaults__
fn.__kwdefaults__ = {}
# Test fn.__get__
fn.__get__ = lambda self, obj: None
# Test fn.__globals__
fn.__globals__ = globals()


class MyClass(object):
    def __init__(self):
        # Test __bases__ attribute
        self.__bases__ = MyClass
        # Test __class__ attribute
        self.__
