fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
# Should throw TypeError
fn()

# Test that a runtime error from the generator's finalizer is caught
def gen():
    try:
        yield 1
        yield 2
    except RuntimeError as err:
        print("Got RuntimeError in gen()", err)
    finally:
        yield 3
        raise RuntimeError("From gen()")
def finalize(gen):
    try:
        raise RuntimeError("From finalize()")
    finally:
        del gen
g = gen()
f = finalizer(g, finalize, g)
next(g)
next(g)
next(g)
del f

# Test that we get a traceback in the generator's finalizer
def gen():
    try:
        yield 1
        yield 2
    except RuntimeError as err:
        print("Got RuntimeError in gen()", err)
    finally:
        yield 3
        print("Raising in gen()")
        raise RuntimeError("From gen()")
def finalize(gen):
    try:
        print("Raising in finalize()")
