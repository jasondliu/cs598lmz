fn = lambda: None
# Test fn.__code__ to see if it's a code object.
NamedTuple.register_fn(lambda x: None)
# Test fn.__code__ to see if it's a code object.
NamedTuple.register_fn(lambda x, *a: None)
# Test fn.__code__ to see if it's a code object.
NamedTuple.register_fn(lambda x, *a, **aa: None)
# Test fn.__code__ to see if it's a code object.
NamedTuple.register_fn(lambda x, **aa: None)
# Test fn.__code__ to see if it's a code object.
NamedTuple.register_fn(lambda x, y: None)
# Test fn.__code__ to see if it's a code object.
NamedTuple.register_fn(lambda x, y=None: None)
# Test fn.__code__ to see if it's a code object.
NamedTuple.register_fn(lambda x, y, **aa: None)
# Test fn.__code__ to see if it's a code object
