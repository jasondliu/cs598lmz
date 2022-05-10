fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27074: __code__ must be a code object.
def fn(): pass
fn.__code__ = None
try:
    fn()
except TypeError as e:
    assert str(e) == "__code__ must be a code object"
else:
    assert False, "TypeError not raised"

# Issue #27074: __code__ must be a code object.
def fn(): pass
fn.__code__ = "not a code object"
try:
    fn()
except TypeError as e:
    assert str(e) == "__code__ must be a code object"
else:
    assert False, "TypeError not raised"

# Issue #27074: __code__ must be a code object.
def fn(): pass
fn.__code__ = 1
try:
    fn()
except TypeError as e:
    assert str(e) == "__code__ must be a code object"
else:
    assert False, "TypeError not raised"

# Issue #27074: __code__ must be
