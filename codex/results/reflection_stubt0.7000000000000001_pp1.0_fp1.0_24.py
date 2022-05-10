fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# pytest.raises(TypeError, lambda: fn())
# pytest.raises(TypeError, lambda: fn.__code__)
# pytest.raises(TypeError, lambda: fn.__code__.co_code)

# TODO: should raise TypeError, but do not
# pytest.raises(TypeError, fn.__code__.__getattribute__, 'co_code')

# pytest.raises(TypeError, lambda: fn.__code__.co_argcount)
# pytest.raises(TypeError, lambda: fn.__code__.__getattribute__, 'co_argcount')

# pytest.raises(AttributeError, getattr, fn.__code__, 'foo')

# TODO: should raise AttributeError, but do not
# pytest.raises(AttributeError, fn.__code__.__getattribute__, 'foo')

# pytest.raises(AttributeError, lambda: fn.__code__.co_argcount.foo)
# pytest.
