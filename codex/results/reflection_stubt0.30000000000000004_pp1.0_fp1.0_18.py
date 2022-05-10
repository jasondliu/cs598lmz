fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #1799: segfault in PyEval_EvalFrameEx()
def f():
    def g():
        raise Exception
    return g
f()()

# Issue #1801: segfault in PyEval_EvalCodeEx()
def f():
    def g():
        return 1
    return g
f()()

# Issue #1802: segfault in PyEval_EvalCodeEx()
def f():
    def g():
        return 1
    return g
f()()

# Issue #1803: segfault in PyEval_EvalCodeEx()
def f():
    def g():
        return 1
    return g
f()()

# Issue #1804: segfault in PyEval_EvalCodeEx()
def f():
    def g():
        return 1
    return g
f()()

# Issue #1805: segfault in PyEval_EvalCodeEx()
def f():
    def g():
