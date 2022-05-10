fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #11894: test that the __code__ attribute of a function can be set to
# None.
def f():
    pass
f.__code__ = None

# Issue #11894: test that the __code__ attribute of a function can be set to a
# non-code object.
def f():
    pass
f.__code__ = object()

# Issue #11894: test that the __code__ attribute of a function can be set to a
# code object with a different number of arguments.
def f(a):
    pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# Issue #11894: test that the __code__ attribute of a function can be set to a
# code object with a different number of local variables.
def f():
    a = 1
f.__code__ = type(f.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0
