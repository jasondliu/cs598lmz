import types
types.MethodType(lambda self, *args: 0, None)

class C(object):
    def foo(self):
        return 0

types.MethodType(C.foo, None)


class F(object):
    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return obj.foo

class C(object):
    bar = F()
    def foo(self):
        return 0

types.MethodType(C.bar, None)

# a function that takes a single argument
def f(x):
    pass

# a class with a single method __call__
class C:
    def __call__(self, x):
        pass

class D(C):
    pass

# test the type of unbound methods

types.MethodType(f, None)
types.MethodType(C(), None)
types.MethodType(C, None)
types.MethodType(D(), None)
types.MethodType(D, None)

# check that we can't apply a function to a class
