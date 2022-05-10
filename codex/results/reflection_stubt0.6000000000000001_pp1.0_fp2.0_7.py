fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = []
fn.__code__.co_lnotab = gi.gi_code.co_lnotab = b'\x00'

# Issue #11649: don't segfault on invalid co_lnotab
sys.settrace(lambda *args: None)
fn()
gi.__next__()

# Issue #13701: don't segfault on invalid co_lnotab
# (negative size)
fn.__code__.co_lnotab = gi.gi_code.co_lnotab = b'\x00\xff'

# Issue #13701: don't segfault on invalid co_lnotab
# (negative size)
fn.__code__.co_lnotab = gi.gi_code.co_lnotab = b'\x00\x00\xff'

# Issue #13701: don't segfault on invalid co_lnotab
# (negative size)
fn.__code__.co_lnotab = gi.gi_code.
