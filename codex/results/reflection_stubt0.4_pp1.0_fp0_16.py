fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# The following test case is based on the one from issue #3693.
def f():
    def g():
        print(1)
        yield
        print(2)
    g()
f()

# The following test case is based on the one from issue #4228.
def f():
    def g():
        yield
    g()
f()

# The following test case is based on the one from issue #4228.
def f():
    def g():
        yield
    g()
f()

# The following test case is based on the one from issue #4228.
def f():
    def g():
        yield
    g()
f()

# The following test case is based on the one from issue #4228.
def f():
    def g():
        yield
    g()
f()

# The following test case is based on the one from issue #4228.
def f():
    def g():
        yield
    g()
f()

# The following test case is based on the one
