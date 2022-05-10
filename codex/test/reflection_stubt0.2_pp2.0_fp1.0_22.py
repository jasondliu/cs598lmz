fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'fn'

# Create a function with a closure
def make_fn():
    x = 1
    def fn():
        return x
    return fn

fn = make_fn()
