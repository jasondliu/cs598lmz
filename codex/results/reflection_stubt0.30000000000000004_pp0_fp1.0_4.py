fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# should raise TypeError: 'generator' object is not callable
# but instead raises SystemError: generator raised StopIteration

# This is because the generator is not checked to be callable
# in the code object's __call__ method.

# This is fixed in Python 3.2.
