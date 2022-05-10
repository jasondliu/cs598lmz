import types
# Test types.FunctionType is non-None before trying to patch.
from types import FunctionType
def patch_function(function, _old_function=None, **kwargs):
    if getattr(function, 'im_class', None) is not None:
        # Handle old-style class instances that have been 2to3'd
        return patch_method(function, **kwargs)
    if isinstance(function, FunctionType) and FunctionType is not None:
        # Function instance
        if not _old_function:
            if hasattr(function, 'func_name'):
                _old_function = function.func_name
            else:
                _old_function = function.__name__
    return decorator(function, **kwargs)

try:
    from types import MethodType
except ImportError:
    # Python 2.1
    # FIXME: probably doesn't work in Python 2.2
    def _FailedPatcher(function, _old_function, **kwargs):
        raise Exception, "Monkey patching is not supported in this version of Python"
    patch_method = patch_function =
