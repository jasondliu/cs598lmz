import types
# Test types.FunctionType too.

from test import support
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure

# This decorator applies the test script to methods.
def setup_with_builtin_decorator(dec):
    def decorate(fn):
        @wraps(fn)
        # On Windows, you can't rename built-in modules, so wrapping os in
        # another module fails.
        def newfunc(*args, **kwargs):
            with support.swap_attr(builtins, dec.__name__, dec):
                return fn(*args, **kwargs)
        return newfunc
    return decorate

def validate(self, new_fn, wrapped=None):
    class C:
        pass

    if wrapped is None:
        wrapped = new_fn
    func = getattr(new_fn, '__wrapped__', None)
    assert_equal(func.__name__, wrapped.__name__)
    assert_equal(func.__doc__, wrapped.__doc
