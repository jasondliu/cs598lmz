fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Make sure that the generator does not get collected
# before the code object.
def f():
    yield 42

def g():
    f().__next__()

# We need to create a new module to avoid the code object
# being kept alive by the module dict.
