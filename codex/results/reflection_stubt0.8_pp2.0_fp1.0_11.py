fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

assert fn.__code__

# Make sure it's not optimized away
assert fn.__code__ == gi.gi_code

print("[DONE]")
