fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_co_flags
def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__.co_flags == 0

def f(): pass
assert f.__code__
