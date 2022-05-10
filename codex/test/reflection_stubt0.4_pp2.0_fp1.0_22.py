fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# This is the only way to get a code object from a generator
# object in Python 3.
def get_code_object(gen):
    return gen.gi_code

