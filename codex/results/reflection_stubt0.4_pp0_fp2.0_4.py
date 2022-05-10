fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as e:
    assert str(e) == "code object passed to FunctionType() must be a code object"
