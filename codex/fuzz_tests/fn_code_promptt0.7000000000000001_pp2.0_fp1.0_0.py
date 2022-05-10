fn = lambda: None
# Test fn.__code__.co_firstlineno == 1 when fn is a lambda.
lambda_code_co_firstlineno_test.__doc__ = """Test fn.__code__.co_firstlineno == 1 when fn is a lambda."""


def f_code_co_firstlineno_test():
    """Test fn.__code__.co_firstlineno == 1 when fn is a function."""
    def f():
        pass
    return f.__code__.co_firstlineno == 1


def has_func_code_co_firstlineno():
    """Test whether the `f.__code__.co_firstlineno` attribute is available."""
    try:
        f = lambda: None
        return f.__code__.co_firstlineno == 1
    except AttributeError:
        return False


def get_firstlineno(f):
    """Get the first line number of f."""
    if has_func_code_co_firstlineno():
        return f.__code__.co_firstlineno
    else:
        return get_source
