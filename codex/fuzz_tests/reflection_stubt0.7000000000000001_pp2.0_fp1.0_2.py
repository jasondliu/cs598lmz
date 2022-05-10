fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()  # should not loop

# check that a function is not callable from a generator
def make_generator():
    yield 1
    raise TypeError("GeneratorExit")

def g():
    gen = make_generator()
    next(gen)
    # this should raise a TypeError
    return gen()

g()
