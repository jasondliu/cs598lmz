fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_running = True
fn()

# This test is for a bug that caused a hang in the interpreter.
# The bug was triggered by a gi_running flag that was set to true
# by a generator that had been destroyed.
def f(x):
    yield x
    yield x
    raise StopIteration
def g():
    return f(1)
def h():
    return g()
def i():
    try:
        return h()
    finally:
        pass
for x in i():
    pass

# This test checks that __getitem__ on a generator object raises
# a TypeError
def gen():
    yield 1
try:
    gen().__getitem__(0)
except TypeError:
    pass
else:
    print "should have raised a TypeError"

# Test that the "gi_frame" field is set correctly
def gen():
    yield 1
    yield 2
g = gen()
next(g)
assert g.gi_frame.f_lasti == -1
next(g)
assert g.gi_
