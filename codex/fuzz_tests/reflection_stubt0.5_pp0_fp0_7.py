fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Should raise TypeError
fn()

# Should raise TypeError
fn.__code__ = None

# Should raise TypeError
fn.__code__ = 42

# Should raise TypeError
fn.__code__ = "a"

# Should raise TypeError
fn.__code__ = {}

# Should raise AttributeError
fn.__code__ = gi

# Should raise AttributeError
fn.__code__ = gi.gi_code

# Should raise TypeError
fn.__code__ = gi.gi_frame

# Should raise TypeError
fn.__code__ = gi.gi_running

# Should raise TypeError
fn.__code__ = gi.gi_yieldfrom

# Should raise TypeError
fn.__code__ = gi.__next__

# Should raise TypeError
fn.__code__ = gi.send

# Should raise TypeError
fn.__code__ = gi.throw

# Should raise TypeError
fn.__code__ = gi.close

#
