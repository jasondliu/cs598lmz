fn = lambda: None
# Test fn.__code__.co_varnames to see if it's bound to something with local variables
# (like a class or a def)
test_fn.__code__.co_varnames

class Test:

    def __init__(self, x):
        self.x = x

test_fn.__code__.co_varnames

def test_fn(x):
    y = x + 1
    return y

test_fn.__code__.co_varnames

test_fn.__code__.co_varnames = ('a', 'b')

test_fn.__code__.co_varnames

test_fn.__code__.co_varnames = ('x',)

test_fn(10)

def test_fn(x):
    y = x + 1
    return y

test_fn.__code__.co_varnames = ('x', 'y')

test_fn(10)

def test_fn(x):
    y = x + 1
    return y

test_fn.
