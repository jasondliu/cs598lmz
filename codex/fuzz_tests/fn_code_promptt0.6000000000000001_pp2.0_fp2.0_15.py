fn = lambda: None
# Test fn.__code__, fn.__closure__, fn.__dict__, fn.__globals__
# fn.__name__, fn.__self__, fn.__class__
# fn.__defaults__, fn.__kwdefaults__
# fn.__annotations__
# fn.__qualname__, fn.__module__, fn.__text_signature__, fn.__doc__

def function(arg1, arg2=None, *, kwarg1=True, kwonlyarg=None):
    """This is a test function
    """
    # Test function.__code__, function.__closure__, function.__dict__, function.__globals__
    # function.__name__, function.__self__, function.__class__
    # function.__defaults__, function.__kwdefaults__
    # function.__annotations__
    # function.__qualname__, function.__module__, function.__text_signature__, function.__doc__
    return arg1 + arg2

class Class:
    class_attr
