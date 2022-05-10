fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
b""[0:0]
TypeError: can't use a string pattern on a bytes-like object
"""}

# The process finished with exit code 0 (0x0).
