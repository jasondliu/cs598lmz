fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27071: test that a generator expression can be used as a
# default value for a keyword argument.
def f(a=i for i in ()):
    pass

# Issue #27071: test that a generator expression can be used as a
# default value for a keyword argument.
def f(a=i for i in ()):
    pass

# Issue #27071: test that a generator expression can be used as a
# default value for a keyword argument.
def f(a=i for i in ()):
    pass

# Issue #27071: test that a generator expression can be used as a
# default value for a keyword argument.
def f(a=i for i in ()):
    pass

# Issue #27071: test that a generator expression can be used as a
# default value for a keyword argument.
def f(a=i for i in ()):
    pass

# Issue #27071: test that a generator expression can be used as a
# default value for a keyword argument.
def f(a=i
