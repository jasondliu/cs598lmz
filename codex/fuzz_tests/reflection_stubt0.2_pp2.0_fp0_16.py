fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, not a SystemError
def fn():
    pass
fn.__code__ = None
fn()

# This should raise a TypeError, not a SystemError
def fn():
    pass
fn.__code__ = 1
fn()

# This should raise a TypeError, not a SystemError
def fn():
    pass
fn.__code__ = "abc"
fn()

# This should raise a TypeError, not a SystemError
def fn():
    pass
fn.__code__ = [1, 2, 3]
fn()

# This should raise a TypeError, not a SystemError
def fn():
    pass
fn.__code__ = {1: 2}
fn()

# This should raise a TypeError, not a SystemError
def fn():
    pass
fn.__code__ = (1, 2, 3)
fn()

# This should raise a TypeError, not a SystemError
def fn():
    pass
fn.__code__ = b"abc"
fn()

# This should
