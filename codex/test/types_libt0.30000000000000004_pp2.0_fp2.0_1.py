import types
types.MethodType(lambda self: None, None, object)

# Test for issue #2074
class A(object):
    def __init__(self, x):
        self.x = x
    def __get__(self, obj, objtype):
        return self.x
    def __set__(self, obj, value):
        self.x = value
    def __delete__(self, obj):
        del self.x

class B(object):
    a = A(1)

b = B()
b.a = 2
b.a
del b.a

# Test for issue #2075
class A(object):
    def __init__(self, x):
        self.x = x
    def __get__(self, obj, objtype):
        return self.x
    def __set__(self, obj, value):
        self.x = value
    def __delete__(self, obj):
        del self.x

class B(object):
    a = A(1)

b = B()
b.a = 2
