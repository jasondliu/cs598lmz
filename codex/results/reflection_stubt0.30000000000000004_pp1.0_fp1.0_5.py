fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #19051: segfault with a generator that has a __del__ method
def f():
    yield 1
    yield 2
    yield 3
f.__del__ = lambda: None
for i in f():
    pass

# Issue #19051: segfault with a generator that has a __del__ method
def f():
    yield 1
    yield 2
    yield 3
f.__del__ = lambda: None
list(f())

# Issue #19051: segfault with a generator that has a __del__ method
def f():
    yield 1
    yield 2
    yield 3
f.__del__ = lambda: None
tuple(f())

# Issue #19051: segfault with a generator that has a __del__ method
def f():
    yield 1
    yield 2
    yield 3
f.__del__ = lambda: None
set(f())

# Issue #19051: segfault with a generator that has a __del__ method
def f():
   
