import types
types.MethodType(lambda self: None, None, A)

# This is not a bug, but a feature.  It's a feature because it allows
# you to create a method out of a function that doesn't care about
# the class it's bound to.  It's not a bug because it's not a
# problem if you don't care about the class it's bound to.

# It's also not a bug because it's not a problem if you do care about
# the class it's bound to.  In this case, you can make a closure that
# captures the class:

def make_method(func, cls):
    def method(self, *args):
        return func(cls, *args)
    return method

A.meth = make_method(lambda cls, x: "A: %s" % x, A)
B.meth = make_method(lambda cls, x: "B: %s" % x, B)

a = A()
b = B()

