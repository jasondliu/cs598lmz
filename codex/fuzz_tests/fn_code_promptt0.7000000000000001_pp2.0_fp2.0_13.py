fn = lambda: None
# Test fn.__code__
test_fn.__code__.co_code
test_fn.__code__.co_varnames
test_fn.__code__.co_argcount
test_fn.__code__.co_nlocals
test_fn.__code__.co_flags

# Test fn.__call__
test_fn()

# Test fn.__globals__
test_fn.__globals__['__builtins__']
test_fn.__globals__['__file__']
test_fn.__globals__['__package__']

# Test fn.__closure__
def outer():
    x = 1
    def inner():
        print x
    return inner

fn = outer()
fn.__closure__[0].cell_contents
fn.__closure__[0].cell_contents = 10
fn.__closure__[0].cell_contents

print(fn.__closure__[0].cell_contents)

# Test fn.__get__
class TestClass:
    def __init__(self, x
