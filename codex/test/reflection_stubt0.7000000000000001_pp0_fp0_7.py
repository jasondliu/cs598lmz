fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Make the "co_name" of fn.__code__ be a new-style string, and
# check that the repr() of fn.__code__ doesn't crash.
