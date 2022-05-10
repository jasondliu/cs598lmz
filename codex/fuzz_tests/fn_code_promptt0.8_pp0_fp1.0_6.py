fn = lambda: None
# Test fn.__code__.co_argcount.
assert fn.__code__.co_argcount == 0
# Test fn.__code__.co_code.
assert fn.__code__.co_code == b'|\x00Z\x00d\x01\x83\x01\x01\x00d\x02S'
# Test fn.__code__.co_consts.
assert fn.__code__.co_consts == (None,)
# Test fn.__code__.co_filename.
assert fn.__code__.co_filename == '<string>'
# Test fn.__code__.co_firstlineno.
assert fn.__code__.co_firstlineno == 1
# Test fn.__code__.co_flags.
assert fn.__code__.co_flags == 67
# Test fn.__code__.co_freevars.
assert fn.__code__.co_freevars == ()
# Test fn.__code__.co_lnotab.
assert fn.__code__.co_lnotab == b'\
