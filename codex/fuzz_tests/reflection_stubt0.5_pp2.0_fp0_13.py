fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Issue #22256: Ensure that a generator's code object is not
# garbage collected when the generator is still running.
import gc
def f():
    g = (x for x in [1])
    gc.collect()
    return g
g = f()
next(g)
del g
gc.collect()

# Issue #22257: Ensure that a generator's code object is not
# garbage collected when the generator is still running.
import gc
def f():
    g = (x for x in range(10))
    gc.collect()
    return g
g = f()
next(g)
del g
gc.collect()

# Issue #22258: Ensure that a generator's code object is not
# garbage collected when the generator is still running.
import gc
def f():
    g = (x for x in range(100))
    gc.collect()
    return g
g = f()
next(g)
del g
gc.collect()

# Issue #22259: Ensure that a generator's code object is not
# garbage
