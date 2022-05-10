fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: test that the __code__ attribute of a built-in function
# cannot be set to a non-code object.
def f():
    pass

def g():
    pass

f.__code__ = g

# Issue #24071: test that the __code__ attribute of a built-in function
# cannot be set to a code object with a different name.
def f():
    pass

def g():
    pass

f.__code__ = g.__code__

# Issue #24071: test that the __code__ attribute of a built-in function
# cannot be set to a code object with a different number of arguments.
def f():
    pass

def g(x):
    pass

f.__code__ = g.__code__

# Issue #24071: test that the __code__ attribute of a built-in function
# cannot be set to a code object with a different number of local variables.
def f():
    pass

def g():
    x = 1

f.
