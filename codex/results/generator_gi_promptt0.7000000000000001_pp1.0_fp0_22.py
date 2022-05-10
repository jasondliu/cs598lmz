gi = (i for i in ())
# Test gi.gi_code.co_freevars

def f1(x):
    g = x
    def f2(y): return g + y
    return f2

def f3(y, f): return f(y)

assert f3(2, f1(1)) == 3

# Test gi.gi_code.co_cellvars

def f1(x):
    def f2(y):
        def f3(z):
            return x + y + z
        return f3
    return f2

def f4(z, f):
    return f(z)

r = f4(1, f1(1)(1))
assert r == 3

# Test gi.gi_code.co_flags

def f1(): pass
assert f1.__code__.co_flags == 67

def f2(a, b=3, c=4, *args, **kwargs): pass
assert f2.__code__.co_flags == 131

def f3():
    yield 1
assert f3.__code__.co
