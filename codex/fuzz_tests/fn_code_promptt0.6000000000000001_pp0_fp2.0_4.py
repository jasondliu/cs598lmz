fn = lambda: None
# Test fn.__code__ and fn.__defaults__
# NOTE: __defaults__ is a tuple (immutable)
fn.__code__ = CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
fn.__defaults__ = (1, 2, 3)
fn.__kwdefaults__ = {'a': 1, 'b': 2}

# Test __class__
class C:
    pass

o = C()
o.__class__ = type('C', (object,), {'a': 1})

# Test __closure__
def f():
    a = 1
    b = 2
    c = 3
    def g():
        return a + b + c
    return g

g = f()
g.__code__ = CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', (), ())
g.__closure__ = (a, b, c)

# Test __annotations__
def f():
    a: int = 1

f.__annotations
