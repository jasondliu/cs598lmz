fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# pypy: disable=undefined-variable
assert_raises(TypeError, compile, "", "", "exec")
assert_raises(TypeError, code)
assert_raises(TypeError, code, 0)
assert_raises(TypeError, code, 0, 0)
assert_raises(TypeError, code, 0, 0, 0)
assert_raises(TypeError, code, 0, 0, 0, 0)
assert_raises(TypeError, code, 0, 0, 0, 0, 0)
assert_raises(TypeError, code, 0, 0, 0, 0, 0, 0)
assert_raises(TypeError, code, 0, 0, 0, 0, 0, 0, 0)
assert_raises(TypeError, code, 0, 0, 0, 0, 0, 0, 0, 0)
assert_raises(TypeError, code, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert_raises(TypeError, code, 0, 0, 0, 0, 0, 0
