from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(100))

# Test that we don't leak data from a raise statement when it is
# caught.

# The following should not cause an UnboundLocalError.
try:
    raise Exception
except:
    pass

# Check that the exception and traceback are not leaked across
# generator boundaries.
def f():
    try:
        raise Exception
    except:
        yield

# Check that we don't leak the exception object and traceback across
# generator boundaries.
def f():
    try:
        raise Exception
    except:
        yield

# Check that we don't leak the exception object and traceback across
# generator boundaries.
def f():
    try:
        raise Exception
    except:
        yield

# Check that we don't leak the exception object and traceback across
# generator boundaries.
def f():
    try:
        raise Exception
    except:
        yield

# Check that we don't leak the exception object and traceback across
# generator boundaries.
def f():
    try:
        raise
