fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #13984: test that the __code__ attribute of a function can be
# set to a non-code object.
def f():
    pass
f.__code__ = None

# Issue #14074: test that the __code__ attribute of a function can be
# set to a code object with a different number of arguments.
def f(a, b, c):
    pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               "", "", 0, "", (), (), (), "", "", 0, 0)

# Issue #14074: test that the __code__ attribute of a function can be
# set to a code object with a different number of local variables.
def f(a, b, c):
    pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
