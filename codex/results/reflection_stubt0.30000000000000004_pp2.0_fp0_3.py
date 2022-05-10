fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Test that the code object is not modified
assert fn.__code__.co_code == b''
assert fn.__code__.co_filename == '<unknown>'
assert fn.__code__.co_name == '<lambda>'
assert fn.__code__.co_firstlineno == 1

# Test that the code object is not modified
fn.__code__ = gi.gi_code
assert fn.__code__.co_code == b''
assert fn.__code__.co_filename == '<unknown>'
assert fn.__code__.co_name == '<lambda>'
assert fn.__code__.co_firstlineno == 1

# Test that the code object is not modified
fn.__code__ = gi.gi_code
assert fn.__code__.co_code == b''
assert fn.__code__.co_filename == '<unknown>'
assert fn.__code__.co_name == '<lambda>'
assert fn.__code__.co_firstlineno == 1

