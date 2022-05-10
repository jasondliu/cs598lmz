fn = lambda: None
# Test fn.__code__.co_varnames
# >>> def fn():
# ...     a = 1
# ...     b = 2
# ...     c = 3
# ...
# >>> fn.__code__.co_varnames
# ('a', 'b', 'c')
# Test fn.__code__.co_argcount
# >>> def fn(a, b, c):
# ...     pass
# ...
# >>> fn.__code__.co_argcount
# 3

def get_param_names(fn):
    return fn.__code__.co_varnames[:fn.__code__.co_argcount]

# Test get_param_names
# >>> def fn(a, b, c):
# ...     pass
# ...
# >>> get_param_names(fn)
# ('a', 'b', 'c')


def get_param_values(fn, args):
    param_names = get_param_names(fn)
    return {name: args[i] for i, name in enumerate(param_names)}

# Test get_param
