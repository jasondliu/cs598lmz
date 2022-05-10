fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# test that the code object is not modified
assert fn.__code__.co_code == gi.gi_code.co_code

# test that the code object is not modified even with a different name
gi.gi_code.co_name = 'foobar'
assert fn.__code__.co_name == 'fn'

# test that the code object is not modified even with a different name
gi.gi_code.co_name = 'fn'
assert fn.__code__.co_name == 'fn'

# test that the code object is not modified even with a different name
fn.__code__.co_name = 'foobar'
assert fn.__code__.co_name == 'foobar'

# test that the code object is not modified even with a different name
fn.__code__.co_name = 'fn'
assert fn.__code__.co_name == 'fn'

# test that the code object is not modified even with a different name
fn.__code__.
