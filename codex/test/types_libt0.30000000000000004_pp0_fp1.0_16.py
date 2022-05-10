import types
types.MethodType(lambda self: None, None, None)

# This is a test of the __new__ method of a type.
# The __new__ method is called before __init__, and is responsible
# for returning a new instance of the class.
class A(object):
    def __new__(cls, a, b, c):
        return super(A, cls).__new__(cls)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

# This is a test of the __del__ method of a type.
# The __del__ method is called when an instance is about to be destroyed.
class B(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

