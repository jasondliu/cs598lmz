gi = (i for i in ())
# Test gi.gi_code is created
# and that it doesn't crash when accessed
# (revealed bug in 2.6.0)
gi.gi_code

def f(x=gi):
    return x

assert f() is gi
# Test that gi.gi_code is created
# and that it doesn't crash when accessed
# (revealed bug in 2.6.0)
f().gi_code

def f(x=f()):
    return x

assert f() is f()
# Test that f().gi_code is created
# and that it doesn't crash when accessed
# (revealed bug in 2.6.0)
f().gi_code

def f(x=f):
    return x

assert f() is f

def f():
    return f()

assert f() is f()

class C(object):
    def __get__(self, obj, type=None):
        return self

def f(x=C()):
    return x

assert f() is f()

def f(x=C()):
    raise Exception
