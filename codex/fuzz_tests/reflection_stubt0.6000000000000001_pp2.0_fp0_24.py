fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# assert_exception(TypeError, lambda: fn.__code__)

class F(object):

    def f(self):
        return 1

class C(F):

    def f(self):
        return 2

assert F().f() == 1
assert C().f() == 2

def f():
    return 1

f.__code__ = C().f.__code__

assert f() == 2

def f():
    return 1

f.__code__.co_name = "g"

assert f.__name__ == "g"

# assert_exception(TypeError, lambda: f.__code__.co_name)

def f(a):
    pass

assert f.__code__.co_varnames == ("a",)

def f():
    pass

assert f.__code__.co_varnames == ()

def f(a, b, c):
    pass

assert f.__code__.co_varnames == ("a", "b",
