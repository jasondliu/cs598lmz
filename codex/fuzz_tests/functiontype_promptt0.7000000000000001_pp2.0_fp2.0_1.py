import types
# Test types.FunctionType and types.LambdaType is not working.
# Python 3's types.FunctionType is not compatible with Python 2's types.FunctionType.
# Python 3's types.LambdaType is not compatible with Python 2's types.LambdaType.
_IS_FUNCTION = (
    types.MethodType, types.BuiltinMethodType, types.BuiltinFunctionType,
    types.ModuleType,
)

try:
    # Python 3.x
    _IS_FUNCTION += (types.FunctionType,)
except AttributeError:
    # Python 2.x
    _IS_FUNCTION += (types.FunctionType, types.LambdaType)


def is_function(fn):
    """Check if an object is function type.
    """
    return isinstance(fn, _IS_FUNCTION)


def is_generator(fn):
    """Check if an object is generator type.
    """
    return isinstance(fn, types.GeneratorType)


def is_iterable(obj):
    """Check if an object is iterable.


