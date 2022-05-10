fn = lambda: None
# Test fn.__code__ is not None.
# Test fn.__defaults__ is None.
# Test fn.__code__.co_varnames is ()(empty tuple).
# Test fn.__code__.co_argcount is 0.
# Test fn.__code__.co_filename is '<stdin>'.

def args_test(a1, a2, a3=True, a4=False): pass
# Test fn.__code__ is not None.
# Test fn.__defaults__ is (False,).
# Test fn.__code__.co_varnames is ('a1', 'a2', 'a3', 'a4').
# Test fn.__code__.co_argcount is 4.
# Test fn.__code__.co_filename is '<stdin>'.
# Test fn.__code__.co_flags == 0
# Test fn.__code__.co_flags & CO_VARARGS == 0
# Test fn.__code__.co_flags & CO_VARKEYWORDS == 0
# Test fn.__code__.co_
