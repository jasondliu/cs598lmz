fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute can be deleted
def fn():
    pass
del fn.__code__

# Test that __code__ can be set to None
def fn():
    pass
fn.__code__ = None

# Test that __code__ can be set to a code object
def fn():
    pass
fn.__code__ = fn.__code__

# Test that __code__ can be set to a tuple
def fn():
    pass
fn.__code__ = (1, 2, 3, 4, 5)

# Test that __code__ can be set to a list
def fn():
    pass
fn.__code__ = [1, 2, 3, 4, 5]

# Test that __code__ can be set to a set
def fn():
    pass
fn.__code__ = {1, 2, 3, 4, 5}

# Test that __code__ can be set to a frozenset
def fn():
    pass
fn.__code__ = frozenset([1, 2, 3, 4, 5])
