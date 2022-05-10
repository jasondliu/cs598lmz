fn = lambda: None
# Test fn.__code__.co_flags
setattr(fn, '__code__', type(fn.__code__)(
    0, 0, 0, 0, b'', (), (), (), '', '', 0, b''))
assert fn.__code__.co_flags == 0
setattr(fn, '__code__', type(fn.__code__)(
    0, 0, 0, 0x08, b'', (), (), (), '', '', 0, b''))
assert fn.__code__.co_flags == 8

# 5-tuples for code objects in functions with no defaults
def fn():
    pass
assert fn.__code__.co_argcount == 0
assert fn.__code__.co_kwonlyargcount == 0
assert fn.__code__.co_nlocals == 0
assert fn.__code__.co_stacksize == 2
assert fn.__code__.co_flags == 67

# 7-tuples for code objects in functions with defaults
def fn(a=None):
    pass
assert fn.__code__.co_argcount == 1

