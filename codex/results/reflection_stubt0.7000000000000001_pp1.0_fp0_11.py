fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, b"", b"", (), (), "", b"", 0, b""
)
b = pickle.dumps(fn.__code__)
# Error in the documentation:
# https://docs.python.org/3.1/library/pickle.html#what-can-be-pickled-and-unpickled
# "types.CodeType (version added: 3.2)", but it is present in 3.1
print(repr(pickle.loads(b)))

# Issue #12649: Don't crash when trying to pickle a code object with a
# co_consts tuple containing a code object.
code = types.CodeType(0, 0, 0, 0, b"", b"", (1, 2, 3), (), "", b"", 0, b"")
t = (code,)
code = types.CodeType(0, 0, 0, 0, b"", b"", t, (), "", b"", 0, b"")
try:
    pickle
