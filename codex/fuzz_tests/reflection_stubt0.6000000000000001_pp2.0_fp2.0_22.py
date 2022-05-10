fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# In Python 3, it will raise a TypeError, but in Python 2, it will raise a SystemError
