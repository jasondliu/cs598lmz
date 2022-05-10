fn = lambda: None
# Test fn.__code__
fn.__code__.co_filename
print(fn.__code__.co_filename)
# Test fn.__name__
fn.__name__
fn.__name__ = 'new_name'
# Test fn.__defaults__
fn.__defaults__
fn.__defaults__ = (1, 2, 3)
fn.__defaults__
# Test fn.__globals__
fn.__globals__
print(fn.__globals__)
# Test fn.__closure__
fn.__closure__
fn.__closure__ = (1, 2, 3)
fn.__closure__
# Test fn.__dict__
fn.__dict__
fn.__dict__ = {'a': 1}
fn.__dict__

# Test fn.__code__.__class__
print(fn.__code__.co_filename.__class__)
# Test fn.__name__.__class__
fn.__name__.__class__
# Test fn.__defaults__.__class__
fn.__defaults__
