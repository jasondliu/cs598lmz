fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #12071: test that a generator expression can be used as a
# default value for a keyword argument.
def f(a=i for i in ()):
    pass

# Issue #12071: test that a generator expression can be used as a
# default value for a keyword argument, even if it's not the last
# argument.
def f(a=1, b=i for i in ()):
    pass

# Issue #12071: test that a generator expression can be used as a
# default value for a keyword argument, even if it's not the last
# argument, and even if there are other keyword arguments after it.
def f(a=1, b=i for i in (), c=2):
    pass

# Issue #12071: test that a generator expression can be used as a
# default value for a keyword argument, even if it's not the last
# argument, and even if there are other keyword arguments after it,
# and even if there are positional arguments before it.
def f(a, b=i for i in (), c=
