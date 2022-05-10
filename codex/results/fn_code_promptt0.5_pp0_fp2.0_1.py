fn = lambda: None
# Test fn.__code__
Test.assert_equals(fn.__code__.co_varnames, ('',))
Test.assert_equals(fn.__code__.co_argcount, 0)

@count_args
def fn(a, b=None, *args, c=None, **kwargs):
    pass
# Test fn.__code__
Test.assert_equals(fn.__code__.co_varnames, ('a', 'b', 'c', 'args', 'kwargs'))
Test.assert_equals(fn.__code__.co_argcount, 2)

@count_args
def fn(a, b, c=None, d=None, *args, e=None, f=None, **kwargs):
    pass
# Test fn.__code__
Test.assert_equals(fn.__code__.co_varnames, ('a', 'b', 'c', 'd', 'e', 'f', 'args', 'kwargs'))
Test.assert_equals(fn.__code__.co_argcount, 5)
