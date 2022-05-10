fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #12593: The .__closure__ attribute of a function should be read-only
def f(x):
    def g():
        return x
    g.__closure__ = (1,)
    return g

g = f(42)
try:
    g.__closure__ = (1,)
except TypeError:
    pass
else:
    print("Assignment to __closure__ should fail")

# Issue #12593: The .__closure__ attribute of a function should be read-only
def f(x):
    def g():
        return x
    g.__closure__ = (1,)
    return g

g = f(42)
try:
    del g.__closure__
except TypeError:
    pass
else:
    print("Deletion of __closure__ should fail")

# Issue #12593: The .__code__ attribute of a function should be read-only
def f(x):
    def g():
        return x
    g.__code__ = type(g.__code__
