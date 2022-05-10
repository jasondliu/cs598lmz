fn = lambda: None
# Test fn.__code__.co_filename
assert fn.__code__.co_filename == '<stdin>'
# Test fn.__code__.co_nlocals
assert fn.__code__.co_nlocals == 0
# Test fn.__code__.co_argcount
assert fn.__code__.co_argcount == 0
assert fn.__code__.co_firstlineno == 1
assert fn.__code__.co_flags == 67

def fn2(a, b, c):
    return a + b + c

# Test fn2.__code__.co_filename
assert fn2.__code__.co_filename == '<stdin>'
# Test fn2.__code__.co_nlocals
assert fn2.__code__.co_nlocals == 3
# Test fn2.__code__.co_argcount
assert fn2.__code__.co_argcount == 3
assert fn2.__code__.co_firstlineno == 16
assert fn2.__code__.co_varnames == ('a', 'b
