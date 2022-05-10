fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22897: Don't crash when a generator is used as a code object.
def f():
    yield 1

def g():
    return f().gi_code

g()

# Issue #22897: Don't crash when a generator is used as a code object.
def f():
    yield 1

def g():
    return f().gi_code

g()

# Issue #22897: Don't crash when a generator is used as a code object.
def f():
    yield 1

def g():
    return f().gi_code

g()

# Issue #22897: Don't crash when a generator is used as a code object.
def f():
    yield 1

def g():
    return f().gi_code

g()

# Issue #22897: Don't crash when a generator is used as a code object.
def f():
    yield 1

def g():
    return f().gi_code

g()

# Issue #22897: Don't crash when a generator
