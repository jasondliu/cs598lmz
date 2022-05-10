fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'fn'
fn.__module__ = 'fn'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = None
fn.__annotations__ = {}
fn.__kwdefaults__ = None

# this is an example of a function that is not a builtin function
# but is a function that is not a user-defined function
# (i.e. it is a function that is defined in C)
#
# it is a function that is defined in the `functools` module
# and it is the `partial` function
#
# the `partial` function is a function that creates a new function
# with some of the arguments of another function pre-filled
# and the pre-filled arguments are passed positionally
#
# the `partial` function is a function that returns a function
#
# the `partial` function is a function that returns a function
# that is a closure
#
# the `partial`
