fn = lambda: None
# Test fn.__code__.co_argcount
def f(x, y, z): return len(locals())
check(f(1, 2, 3) == 3)
check(f.__code__.co_argcount == 3)
# Test fn.__code__.co_filename
check(f.__code__.co_filename == __file__)
# Test fn.__code__.co_firstlineno
check(f.__code__.co_firstlineno == inspect.currentframe().f_lineno + 1)

# Test fn.__code__.co_consts
check(f.__code__.co_consts[0] is None)
check(f.__code__.co_consts[1] is len)

# Test fn.__code__.co_varnames
check(f.__code__.co_varnames[0] == 'x')
check(f.__code__.co_varnames[1] == 'y')
check(f.__code__.co_varnames[2] == 'z')
check(f
