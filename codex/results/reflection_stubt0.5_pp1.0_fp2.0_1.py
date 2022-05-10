fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

print(fn.__code__.__class__)
print(gi.__class__)

print(gi.gi_code)
print(fn.__code__.gi_code)
