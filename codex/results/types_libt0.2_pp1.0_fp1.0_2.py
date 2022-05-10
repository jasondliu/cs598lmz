import types
types.MethodType(lambda self: None, None, Foo)

# test for __new__
class Foo(object):
    def __new__(cls):
        return object.__new__(cls)

Foo()

# test for __init__
class Foo(object):
    def __init__(self):
        pass

Foo()

# test for __del__
class Foo(object):
    def __del__(self):
        pass

f = Foo()
del f

# test for __getattr__
class Foo(object):
    def __getattr__(self, name):
        return 42

Foo().bar

# test for __setattr__
class Foo(object):
    def __setattr__(self, name, value):
        pass

Foo().bar = 42

# test for __delattr__
class Foo(object):
    def __delattr__(self, name):
        pass

del Foo().bar

# test for __getattribute__
class Foo(object):
    def __getattribute__(
