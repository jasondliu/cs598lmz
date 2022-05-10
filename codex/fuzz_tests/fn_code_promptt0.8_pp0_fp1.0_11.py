fn = lambda: None
# Test fn.__code__ is present
print("fn.__code__:",fn.__code__)

# Test fn.__defaults__
fn.__defaults__ = (1,2,3)
print("fn.__defaults__:",fn.__defaults__)

# Test fn.__doc__
fn.__doc__ = 'my little function'
print("fn.__doc__:",fn.__doc__)

# Test fn.__globals__
fn.__globals__['new_global'] = 'this is a new global'
print("new_global:",globals()['new_global'])

# Test fn.__name__
fn.__name__ = 'my_fn'
assert fn.__name__ == 'my_fn'

# Test fn.__dict__
print("fn.__dict__:",fn.__dict__)

# Test fn.__module__
fn.__module__ = 'my_module'
assert fn.__module__ == 'my_module'

# Test fn.__closure__
def make_adder
