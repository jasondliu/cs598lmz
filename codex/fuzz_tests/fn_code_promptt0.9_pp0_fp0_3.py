fn = lambda: None
# Test fn.__code__ attribute.
test_fn.__code__.co_name += "yo"
test_fn()
# Tests fn.__code__.co_names
"foo" in test_fn.__code__.co_names
# Tests fn.__code__.co_varnames
"a" in test_fn.__code__.co_varnames

# Test fn.__globals__ attribute.
test_fn.__globals__ is globals()

# Test fn.__defaults__ and fn.__kwdefaults__ attributes
# as well as *args and **kwargs
def test_kw(a, *args, b=1, c=2, **kwargs):
    pass

test_fn.__code__.co_argcount
test_fn.__defaults__
test_fn.__kwdefaults__

test_kw.__code__.co_argcount
(1,) == test_kw.__defaults__
{'b': 1, 'c': 2} == test_kw.__kwdefaults__

# Test variables referenced in
