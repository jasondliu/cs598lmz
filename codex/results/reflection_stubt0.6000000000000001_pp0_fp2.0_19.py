fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test with a function with a 'co_lnotab' attribute
def fn(): pass
fn.__code__.co_lnotab = 1
fn()

# test with a function with a __code__ attribute with a 'co_lnotab' attribute
def fn(): pass
fn.__code__.co_lnotab = 1
fn()
