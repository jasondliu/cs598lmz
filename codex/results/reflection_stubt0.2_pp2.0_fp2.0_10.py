fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24097: Crash when calling a builtin with a keyword-only argument
# with a default value.
def f(*, a=None):
    pass
f()

# Issue #24098: Crash when calling a builtin with a keyword-only argument
# with a default value.
def f(*, a=None):
    pass
f(a=1)

# Issue #24098: Crash when calling a builtin with a keyword-only argument
# with a default value.
def f(*, a=None):
    pass
f(1)

# Issue #24098: Crash when calling a builtin with a keyword-only argument
# with a default value.
def f(*, a=None):
    pass
f(a=1, 2)

# Issue #24098: Crash when calling a builtin with a keyword-only argument
# with a default value.
def f(*, a=None):
    pass
f(a=1, b=2)

# Issue #24098: Crash when calling a builtin
