fn = lambda: None
# Test fn.__code__ and __defaults__
a.fn.__code__ = 3
a.fn.__defaults__ = 3
# Test fn.__closure__
a.fn.__closure__ = 3
# Test fn.__doc__
a.fn.__doc__ = 3
# Test fn.__name__
a.fn.__name__ = 3
# Test fn.__dict__
a.fn.__dict__ = 3
# Test fn.__module__
a.fn.__module__ = 3
# Test fn.__annotations__
a.fn.__annotations__ = 3
# Test fn.__globals__
a.fn.__globals__ = 3

try:
    class C:
        def __new__(cls, arg):
            pass
    c = C(3)
except TypeError:
    pass

# Test new/init in a metaclass setting
class Meta(type):
    def __new__(mcls, name, bases, namespace):
        namespace["__new__"] = lambda cls: 1
        namespace["__init__
