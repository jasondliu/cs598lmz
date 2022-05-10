fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23893: Crash when calling a builtin with a keyword-only argument
# and a keyword argument with a default value.
def f(a, *, b=1):
    pass
f(1, b=2)

# Issue #23893: Crash when calling a builtin with a keyword-only argument
# and a keyword argument with a default value.
def f(a, *, b=1):
    pass
f(1, b=2)

# Issue #23893: Crash when calling a builtin with a keyword-only argument
# and a keyword argument with a default value.
def f(a, *, b=1):
    pass
f(1, b=2)

# Issue #23893: Crash when calling a builtin with a keyword-only argument
# and a keyword argument with a default value.
def f(a, *, b=1):
    pass
f(1, b=2)

# Issue #23893: Crash when calling a builtin with a keyword-only argument
# and a keyword argument with a default value
