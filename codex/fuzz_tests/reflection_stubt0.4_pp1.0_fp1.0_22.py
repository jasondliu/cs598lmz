fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #23804: segfault with a generator that has a __del__ method
def gen():
    yield 1
    yield 2
gen.__del__ = lambda: None
for i in gen():
    pass


# Issue #23806: segfault when calling a generator with a __del__ method
def gen():
    yield 1
    yield 2
gen.__del__ = lambda: None
list(gen())


# Issue #23810: segfault when calling a generator with a __del__ method
# that raises an exception
def gen():
    yield 1
    yield 2
gen.__del__ = lambda: 1/0
list(gen())

# Issue #23809: segfault when calling a generator with a __del__ method
# that raises an exception
def gen():
    yield 1
    yield 2
gen.__del__ = lambda: 1/0
for i in gen():
    pass

# Issue #23811: segfault when calling a generator with a __del__ method
# that raises
