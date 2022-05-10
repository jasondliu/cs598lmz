fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Second example
class MyException(Exception):
    pass

def f():
    raise MyException()

def g():
    return f()

def h():
    return g()

def j():
    return h()

j()

# Third example
def f():
    raise MyException()

def g():
    return f()

def h():
    return g()

def j():
    return h()

j()

# Fourth example
def f():
    raise MyException()

def g():
    return f()

def h():
    return g()

def j():
    return h()

j()

# Fifth example
def f():
    raise MyException()

def g():
    return f()

def h():
    return g()

def j():
    return h()

j()

# Sixth example
def f():
    raise MyException()

def g():
    return f()

def h():
    return g()

def j():
    return
