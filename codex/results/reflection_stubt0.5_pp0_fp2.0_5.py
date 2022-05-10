fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# bug 7
def f():
    yield

f().send(None)

# bug 8
def f():
    return lambda: 1

f()()

# bug 9
def f():
    def g():
        return 1
    return g

f()()

# bug 10
def f():
    return lambda: lambda: 1

f()()()

# bug 11
def f():
    return lambda: lambda: lambda: 1

f()()()()

# bug 12
def f():
    return lambda: lambda: lambda: lambda: 1

f()()()()()

# bug 13
def f():
    return lambda: lambda: lambda: lambda: lambda: 1

f()()()()()()

# bug 14
def f():
    return (lambda: 1)

f()()

# bug 15
def f():
    return (lambda: lambda: 1)

f()()()

# bug 16
def f():
    return (lambda: lambda: lambda: 1)

f()()
