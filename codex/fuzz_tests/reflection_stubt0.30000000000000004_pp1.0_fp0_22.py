fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #22688: check that the code object is not freed
# before the generator.
import weakref

def f():
    g = (i for i in range(10))
    return g.gi_code

code = f()
wr = weakref.ref(code)
del code
import gc
gc.collect()
assert wr() is not None

# Issue #22688: check that the code object is not freed
# before the frame.
def f():
    g = (i for i in range(10))
    return g.gi_frame

frame = f()
wr = weakref.ref(frame.f_code)
del frame
import gc
gc.collect()
assert wr() is not None

# Issue #22688: check that the generator object is not freed
# before the frame.
def f():
    g = (i for i in range(10))
    return g.gi_frame

frame = f()
wr = weakref.ref(frame.f_locals['g'])
del
