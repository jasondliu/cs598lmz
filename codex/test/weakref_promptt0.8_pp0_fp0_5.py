import weakref
# Test weakref.ref
def f(x):
    return x
foo = lambda x:x
x = weakref.ref(f)(foo)
