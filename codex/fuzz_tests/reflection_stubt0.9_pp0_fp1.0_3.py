fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()
# AttributeError: 'generator' object has no attribute 'co_firstlineno'
