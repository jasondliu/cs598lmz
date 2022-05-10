fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# this should not crash
fn()

gi = (i for i in ())
# this should not crash
fn.__code__ = gi
fn()

gi = (i for i in ())
try:
    # this should not 
