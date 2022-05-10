fn = lambda: None
# Test fn.__code__.co_firstlineno
def test_fn():
    pass

class TestClass:
    def test_method(self):
        pass

def test_fn2():
    pass

test_fn.__code__.co_firstlineno

TestClass.test_method.__code__.co_firstlineno

test_fn2.__code__.co_firstlineno

# Test fn.__code__.co_varnames
def test_fn(a, b, c):
    pass

test_fn.__code__.co_varnames

# Test fn.__code__.co_argcount
def test_fn(a, b, c):
    pass

test_fn.__code__.co_argcount

# Test fn.__code__.co_argcount
def test_fn(a, b, c):
    pass

test_fn.__code__.co_argcount

# Test fn.__code__.co_argcount
def test_fn(a, b, c):
    pass


