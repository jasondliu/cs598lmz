fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator can be used as a code object.
# This is a regression test for a bug in the JIT.
def f():
    yield 1

def g():
    return f().__code__

def h():
    return g()

assert h() is f.__code__

# Test that a generator can be used as a code object.
# This is a regression test for a bug in the JIT.
def f():
    yield 1

def g():
    return f().gi_frame.f_code

def h():
    return g()

assert h() is f.__code__

# Test that a generator can be used as a code object.
# This is a regression test for a bug in the JIT.
def f():
    yield 1

def g():
    return f().gi_frame.f_code.co_name

def h():
    return g()

assert h() == 'f'

# Test that a generator can be used as a code object.
# This is a regression test for a
