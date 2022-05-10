fn = lambda: None
# Test fn.__code__.co_varnames
test_fn.__code__.co_varnames = (1, )
# Test fn.__code__.co_filename
test_fn.__code__.co_filename = 'test'
# Test fn.__code__.co_firstlineno
test_fn.__code__.co_firstlineno = 'test'
# Test fn.__code__.co_lnotab
test_fn.__code__.co_lnotab = 'test'
# Test fn.__code__.co_freevars
test_fn.__code__.co_freevars = (1, )
# Test fn.__code__.co_cellvars
test_fn.__code__.co_cellvars = (1, )

# Test userdict.UserDict
class TestUserDict(UserDict):
    def __missing__(self):
        return 1

# Test functools.partial
def test_partial():
    def test_partial_fn(a, b):
        return a + b

    yield partial
