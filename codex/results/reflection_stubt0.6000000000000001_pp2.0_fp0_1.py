fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This is the same as above, but the inner generator
# is created in a function scope, so we have to use
# the gi_frame attribute to get the frame.

def f():
    return (i for i in ())

fn = lambda: None
gi = f()
fn.__code__ = gi.gi_frame.f_code
fn()
