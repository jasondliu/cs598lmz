fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Create a function that takes a function and a tuple of arguments, and calls
# the function with those arguments.
def call_fn(fn, args):
    return fn(*args)

# Create a function that takes a function and a tuple of arguments, and calls
# the function with those arguments.
def call_fn_with_kwargs(fn, args):
    return fn(**args)

# Create a function that takes a function and a tuple of arguments, and calls
# the function with those arguments.
def call_fn_with_kwargs_and_starargs(fn, args):
    return fn(**args, *args)

# Create a function that takes a function and a tuple of arguments, and calls
# the function with those arguments.
def call_fn_with_kwargs_and_starargs_and_kwargs(fn, args):
    return fn(**args, *args, **args)

# Create a function that takes a function and a tuple of arguments, and calls
# the function with those arguments.
def call_fn_with_kwargs_and_
