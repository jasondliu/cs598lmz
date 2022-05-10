fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# __code__ is a read-only attribute
with raises(TypeError):
    fn.__code__ = 42

# __code__ is a read-only attribute
with raises(TypeError):
    del fn.__code__

# Code objects are immutable
with raises(TypeError):
    fn.__code__.co_code = 42

# Code objects are immutable
with raises(TypeError):
    del fn.__code__.co_code

# Code objects are immutable
with raises(TypeError):
    fn.__code__.co_argcount = 42

# Code objects are immutable
with raises(TypeError):
    del fn.__code__.co_argcount

# Code objects are immutable
with raises(TypeError):
    fn.__code__.co_varnames = 42

# Code objects are immutable
with raises(TypeError):
    del fn.__code__.co_varnames

# Code objects are immutable
with raises(TypeError):
    fn.__code__.co_filename = 42

# Code objects are
