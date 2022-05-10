fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Make sure we're using the new iterator in the new code object
# even if it doesn't have a .gi_code attribute
class A(object):
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 3:
            raise StopIteration
        self.i += 1
        return self.i

# This should use the new iterator protocol
def new_fn():
    for x in A():
        yield x

fn.__code__ = new_fn.__code__

# This should also use the new iterator protocol
def new_fn2():
    x = A()
    if x:
        yield 1

fn.__code__ = new_fn2.__code__

# This should use the old iterator protocol
def old_fn():
    yield 1

fn.__code__ = old_fn.__code__

# The outer loop uses the new iterator protocol, and the inner
# loop uses the old
