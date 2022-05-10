fn = lambda: None
# Test fn.__code__.co_cellvars
try:
    exec("""def fn():
    x = 0
    def inner():
        x = 0
    inner()""", globals())
    fn.__code__.co_cellvars
except AttributeError:
    pass
else:
    raise AssertionError

def fn():
    x = 0
    def inner():
        x = 0
    inner()

# Test fn.__code__.co_cellvars and fn.__code__.co_freevars
def fn():
    x = 0
    y = 0
    def inner():
        x = 0
        y = 0
    inner()

# Test fn.__code__.co_cellvars and fn.__code__.co_freevars
def fn():
    def inner(): pass
    def deeper(): nonlocal inner
    deeper()

# Test fn.__code__.co_cellvars and fn.__code__.co_freevars
def fn():
    def inner(): nonlocal outer
    outer = fn
    inner()

