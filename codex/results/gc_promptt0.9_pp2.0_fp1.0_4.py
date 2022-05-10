import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Default args of 100*[None]
def func():
    return tuple(range(100))

# This causes func() to be uncollectable, probably due to recursion.
func.__defaults__ = 100*(func,)

func()
del func
gc.collect()

# Deallocates func_defaults_copy, but not func (since its refcount is now 1)
def func(a=1):
    pass

g = globals()
for name in sorted(g):
    f = g[name]
    if isinstance(f, FunctionType) and name.startswith('func'):
        f()
gc.collect()

globals()['func']()
gc.collect()

# This should be fixed by the change to the frame finalizer in
# Objects/frameobject.c.
del globals()['func']
gc.collect()
