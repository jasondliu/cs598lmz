fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# The following will raise TypeError:
# fn()
#
# But the following will succeed:
