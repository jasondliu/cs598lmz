fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.__code__.co_varnames
fn.__code__.co_varnames
# Test function with arguments
def fn_with_args(a, b):
    return a + b

fn_with_args.__code__.co_varnames
# Test function with kwargs
def fn_with_kwargs(a, b=1):
    return a + b

fn_with_kwargs.__code__.co_varnames
# Test fn.__code__.co_argcount
fn_with_kwargs.__code__.co_argcount
# Test function with varargs
def fn_with_varargs(*args):
    return sum(args)

fn_with_varargs.__code__.co_varnames
# Test function with kwargs
def fn_with_kwargs(**kwargs):
    return sum(kwargs.values())

fn_with_kwargs.__code__.co_varnames
# Test fn.__code__.co_argcount

