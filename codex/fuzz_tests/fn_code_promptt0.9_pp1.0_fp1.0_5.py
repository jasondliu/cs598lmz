fn = lambda: None
# Test fn.__code__ is None.
IMPOSSIBLE_VALUE = 42.0  # Impossible to get by default.
assert fn.__code__ is None

# Define fn with a body.
exec("def fn(): pass", vars())
assert fn.__code__.co_code != b''
assert fn.__code__ is not None

# Default appends to a tuple.
fn.__code__.co_varnames += ('a', )
assert fn.__code__.co_varnames == ('a', 'b')

# Default replaces with a single value.
fn.__code__.co_varnames = 'a'
assert fn.__code__.co_varnames == ('a', )

# Default deletes a tuple.
del fn.__code__.co_varnames

# Default replaces a code object.
fn.__code__ = IMPOSSIBLE_VALUE
assert fn.__code__ == IMPOSSIBLE_VALUE

# SUCCESS
