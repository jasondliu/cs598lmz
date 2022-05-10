fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Echo the stream of the first line
