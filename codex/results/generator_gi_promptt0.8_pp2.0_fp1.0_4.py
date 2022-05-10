gi = (i for i in ())
# Test gi.gi_code is None, which is a proxy for a generator
# being "finished" (see PyGen_NeedsFinalizing()).
# We need to call gi.close() to prevent reassignment of
# gi_code.
gi.close()
del gi

@jit
def f():
    return sys.getrefcount(42)
# We want the first pass through f() to not notice any
# objects being freed, so the third argument to sys.getrefcount()
# is a dead generator.
f()

# The second pass through f() is supposed to see a
# generator, tuple and code block being freed.
import gc; gc.collect()
f()

@jit
def g(i, j):
    if i > 0:
        g(i, j)
    else:
        g(j, i)
g(5, 2)
gc.collect()
g(5, 2)
