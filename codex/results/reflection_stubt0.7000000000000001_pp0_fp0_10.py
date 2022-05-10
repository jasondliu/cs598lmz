fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# This causes a segfault
# fn.__code__ = gi.gi_code
fn()

# Calling a C function that returns a Generator,
# then calling the Generator with no arguments
def g():
    yield
fn = lambda: None
gi = g()
fn.__code__ = gi.gi_code
gi.gi_frame = fn.__code__.co_consts[0]
fn()

# Calling a C function that returns a Generator,
# then calling the Generator with two arguments
def g():
    yield
fn = lambda: None
gi = g()
fn.__code__ = gi.gi_code
gi.gi_frame = fn.__code__.co_consts[0]
# This causes a segfault
# fn(1, 1)
fn()

# This doesn't cause a segfault:
# Calling a C function that returns a Generator,
# then calling the Generator with one argument
#def g():
#    yield
#fn = lambda: None
#gi = g()
#
