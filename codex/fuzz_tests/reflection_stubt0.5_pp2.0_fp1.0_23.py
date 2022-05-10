fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# This should not raise an exception
fn()

# This should not raise an exception
fn.__code__ = None
fn()

# This should not raise an exception
fn.__code__ = gi.gi_code
fn()
