fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Verify the failure message

try:
    fn()
except TypeError as e:
    assert str(e).startswith("code object")
else:
    assert False, "Did not raise"
