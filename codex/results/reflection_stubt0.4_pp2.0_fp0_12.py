fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_call_with_kwargs
def fn(a, b, c):
    return a + b + c
fn(a=1, b=2, c=3)

# test_call_with_kwargs_and_starargs
def fn(a, b, c):
    return a + b + c
fn(1, *(2, 3), **{})

# test_call_with_kwargs_and_starargs_and_kwargs
def fn(a, b, c):
    return a + b + c
fn(1, *(2, 3), **{'c': 4})

# test_call_with_kwargs_and_starargs_and_kwargs_and_defaults
def fn(a, b, c=3):
    return a + b + c
fn(1, *(2,), **{'c': 4})

# test_call_with_kwargs_and_starargs_and_kwargs_and_defaults_and_varargs
def fn(a, b
