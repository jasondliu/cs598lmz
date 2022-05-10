fn = lambda: None
# Test fn.__code__.co_varnames
def __test_fn():
    a, b = 1, 2
__test_fn()
del __test_fn

def fn_to_pattern(fn):
    """
    Return arguments + default arguments from function
    as an ArgumentsPattern.
    """
    patterns = [pattern.ArgumentsPattern(sig.Argument(arg, None)) for arg in fn.__code__.co_varnames]
    for i, default in zip(range(fn.__code__.co_argcount - len(fn.__defaults__), fn.__code__.co_argcount), fn.__defaults__):
        patterns[i] = patt
