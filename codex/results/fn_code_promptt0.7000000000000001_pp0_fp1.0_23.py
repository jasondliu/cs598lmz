fn = lambda: None
# Test fn.__code__.co_name
def fn(): pass
assert fn.__code__.co_name == 'fn'
assert fn.__code__.co_argcount == 0
assert fn.__code__.co_varnames == ()
assert fn.__code__.co_flags == 67

# Test fn.__code__.co_varnames
def fn(a): pass
assert fn.__code__.co_name == 'fn'
assert fn.__code__.co_argcount == 1
assert fn.__code__.co_varnames == ('a',)
assert fn.__code__.co_flags == 67

# Test fn.__code__.co_varnames
def fn(a, b, c=4, d=5): pass
assert fn.__code__.co_name == 'fn'
assert fn.__code__.co_argcount == 4
assert fn.__code__.co_varnames == ('a', 'b', 'c', 'd')
assert fn.__code__.co_flags == 67

# Test fn.__
