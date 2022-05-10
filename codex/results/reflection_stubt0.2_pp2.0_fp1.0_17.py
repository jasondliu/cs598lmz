fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator can be used as a function
def f():
    yield 1
    yield 2
    yield 3

assert f()() == 1
assert f()() == 2
assert f()() == 3

# Test that a generator can be used as a function
def f():
    yield 1
    yield 2
    yield 3

assert f()() == 1
assert f()() == 2
assert f()() == 3

# Test that a generator can be used as a function
def f():
    yield 1
    yield 2
    yield 3

assert f()() == 1
assert f()() == 2
assert f()() == 3

# Test that a generator can be used as a function
def f():
    yield 1
    yield 2
    yield 3

assert f()() == 1
assert f()() == 2
assert f()() == 3

# Test that a generator can be used as a function
def f():
    yield 1
    yield 2
    yield 3

assert f()() == 1
assert f()() == 2
assert
