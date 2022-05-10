fn = lambda: None
# Test fn.__code__
assert fn.__code__.co_name == '<lambda>'
assert fn.__code__.co_argcount == 0
assert fn.__code__.co_firstlineno == 1
assert fn.__code__.co_lnotab == b''

def fn(): pass
# Test fn.__code__
assert fn.__code__.co_name == 'fn'
assert fn.__code__.co_argcount == 0
assert fn.__code__.co_firstlineno == 1
assert fn.__code__.co_lnotab == b''

def fn(a): pass
# Test fn.__code__
assert fn.__code__.co_name == 'fn'
assert fn.__code__.co_argcount == 1
assert fn.__code__.co_firstlineno == 1
assert fn.__code__.co_lnotab == b''

def fn(a, b, c): pass
# Test fn.__code__
assert fn.__code__.co_name == 'fn'
assert fn.__code__.
