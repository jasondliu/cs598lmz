import types
types.MethodType(lambda self: None, None)

# __new__
class A(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

# __getattribute__
class A(object):
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

# __getattr__
class A(object):
    def __getattr__(self, name):
        return object.__getattr__(self, name)

# __setattr__
class A(object):
    def __setattr__(self, name, value):
        return object.__setattr__(self, name, value)

# __delattr__
class A(object):
    def __delattr__(self, name):
        return object.__delattr__(self, name)

# __get__
