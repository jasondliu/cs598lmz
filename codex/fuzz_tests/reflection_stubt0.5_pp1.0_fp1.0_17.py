fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a more complex example that checks that we don't crash when
# there are no arguments to the call.

def f(a):
    a(1)

def g():
    pass

f(g)

# This is a more complex example that checks that we don't crash when
# there are keyword arguments to the call.

def f(a):
    a(x=1)

def g(x):
    pass

f(g)

# This is a more complex example that checks that we don't crash when
# there are keyword arguments to the call and the function takes
# **kwargs.

def f(a):
    a(x=1)

def g(**kwargs):
    pass

f(g)

# This is a more complex example that checks that we don't crash when
# there are keyword arguments to the call and the function takes
# *args.

def f(a):
    a(x=1)

def g(*args):
    pass

f(g)

#
