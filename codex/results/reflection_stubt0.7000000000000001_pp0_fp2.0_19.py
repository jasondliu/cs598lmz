fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Code objects may be called with a tuple of arguments
def kw(a, b):
	return a, b
code = type(kw.__code__)(0, 0, 0, 0, b"\x00\x00\x00\x00",
	b"<string>", b"kw", b"", 0, b"\x00\x00\x00\x00")
print(code((1, 2), {}))

# Code objects may be called with a dict of keyword arguments
def kw(a, b):
	return a, b
code = type(kw.__code__)(0, 0, 0, 0, b"\x00\x00\x00\x00",
	b"<string>", b"kw", b"", 0, b"\x00\x00\x00\x00")
print(code((), {"a": 1, "b": 2}))

# The code object may be called with no arguments
def kw(a, b):
	return a, b
code
