fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
assert done

# This used to crash the interpreter.
def fn(a):
    try:
        a.__len__().__getattr__('foo')
    except AttributeError as e:
        pass

fn(range(10))

def f():
    raise 0

def g():
    raise 1

def h():
    try:
        f()
    except f.__code__.co_consts[0]:
        g()

try:
    h()
except TypeError as e:
    assert str(e) == "'NoneType' object is not subscriptable"

def f(): pass
def g(): pass
def h(): pass
def i(): pass

f.__code__.co_consts = (f, g, h, i)

def k():
    return tuple(f.__code__.co_consts)

assert k() == (f, g, h, i)

# make sure we can use a generator as the default parameter value
def f(a=i for i in
