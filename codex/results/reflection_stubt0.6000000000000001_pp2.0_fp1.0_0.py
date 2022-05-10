fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_call_with_kwargs
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn(a=1)

# test_call_with_kwargs_and_starargs
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn(1, 2, a=1)

# test_call_with_kwargs_and_starargs_and_kwargs
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn(1, 2, a=1, b=2)

# test_dunder_call
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__call__()

# test_dunder_call_with_args
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__call__(1, 2)

# test_dunder_call
