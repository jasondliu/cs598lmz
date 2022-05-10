fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18250: crash when __code__ is set to a tuple
def fn(): pass
fn.__code__ = (1, 2, 3, 4, 5)
fn()

# Issue #18250: crash when __code__ is set to a list
def fn(): pass
fn.__code__ = [1, 2, 3, 4, 5]
fn()

# Issue #18250: crash when __code__ is set to a dict
def fn(): pass
fn.__code__ = {'a': 1, 'b': 2}
fn()

# Issue #18250: crash when __code__ is set to a set
def fn(): pass
fn.__code__ = {1, 2, 3}
fn()

# Issue #18250: crash when __code__ is set to a frozenset
def fn(): pass
fn.__code__ = frozenset([1, 2, 3])
fn()

# Issue #18250: crash when __code__ is set to a memoryview
def fn(): pass
fn.__code__ = memoryview
