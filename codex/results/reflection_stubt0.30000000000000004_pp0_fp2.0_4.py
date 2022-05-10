fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17056: Make sure that the code object of a generator is
# not modified when the generator is closed.

import gc

def gen():
    yield 1

g = gen()
next(g)
g.close()
gc.collect()
assert g.gi_frame.f_code is gen.__code__

# Issue #17056: Make sure that the code object of a generator is
# not modified when the generator is exhausted.

def gen():
    yield 1

g = gen()
next(g)
next(g, None)
gc.collect()
assert g.gi_frame.f_code is gen.__code__

# Issue #17056: Make sure that the code object of a generator is
# not modified when the generator raises an exception.

def gen():
    yield 1

g = gen()
next(g)
try:
    g.throw(ValueError)
except ValueError:
    pass
gc.collect()
assert g.gi_frame.f_code is gen.__code
