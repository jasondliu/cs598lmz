fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: segfault when an exception is raised in a generator
# that is being finalized.
def f():
    try:
        yield
    except:
        pass

def g():
    for i in range(2):
        yield from f()

try:
    g().throw(ZeroDivisionError)
except ZeroDivisionError:
    pass

# Issue #23897: segfault when an exception is raised in a generator
# that is being finalized.
def f():
    try:
        yield
    except:
        pass

def g():
    for i in range(2):
        yield from f()

try:
    g().close()
except ZeroDivisionError:
    pass

# Issue #23897: segfault when an exception is raised in a generator
# that is being finalized.
def f():
    try:
        yield
    except:
        pass

def g():
    for i in range(2):
        yield from f()

try:
    g
