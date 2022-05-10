fn = lambda: None
gi = (i for i in ())
fn.__code__ = c
fn.__globals__ = {"gi": gi}
fn.__closure__ = (gi,)

# Make sure that globals and closure are correctly set to the
# builtin CodeType
exec("pass", gc)
assert fn.__code__ == CodeType(0, 0, 0, 0, b"", (), (), (), "", "", 0, b"")
assert fn.__globals__ == {}
assert fn.__closure__ is None

# Make sure that the code object is correctly set to the builtin
# CodeType, and that it is shared between the different functions
def g():
    pass

assert f.__code__ == CodeType(0, 0, 0, 0, b"", (), (), (), "", "", 0, b"")
assert g.__code__ == f.__code__
assert f.__globals__ == {}
assert f.__closure__ is None
