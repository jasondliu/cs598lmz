fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the exception is not wrapped in an extra exception
# (see issue #16862)
try:
    fn()
except RuntimeError as e:
    assert str(e) == "generator didn't yield"
else:
    raise AssertionError("expected RuntimeError")

# Test that the exception is not wrapped in an extra exception
# (see issue #16862)
try:
    fn()
except RuntimeError as e:
    assert str(e) == "generator didn't yield"
else:
    raise AssertionError("expected RuntimeError")

# Test that the exception is not wrapped in an extra exception
# (see issue #16862)
try:
    fn()
except RuntimeError as e:
    assert str(e) == "generator didn't yield"
else:
    raise AssertionError("expected RuntimeError")

# Test that the exception is not wrapped in an extra exception
# (see issue #16862)
try:
    fn()
except RuntimeError as e:
    assert str(e) ==
