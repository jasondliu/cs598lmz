fn = lambda: None
gi = (i for i in ())
fn.__code__ = b'\x01\x00\x00\x00\x00\x00\x00\x00'
gi.gi_code = fn.__code__
gi.gi_frame = fn.__code__
