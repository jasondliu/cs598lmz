fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# Uncomment the following lines and comment the previous line to see that
# `fn.__code__` is a generator
"""
def fn():
    yield
fn.__code__ = fn()
"""
</code>

