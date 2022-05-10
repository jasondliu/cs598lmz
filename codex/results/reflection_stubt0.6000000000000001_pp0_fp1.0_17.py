fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__call__()
# segfaults
#fn()

print("[OK]")
