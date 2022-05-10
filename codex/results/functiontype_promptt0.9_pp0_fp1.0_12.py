import types
# Test types.FunctionType and types.LambdaType

global __doctest_global_ns
__doctest_global_ns = {}

def _check_types(func, ftype):
    """Check that a function exists, is a class of type ftype, and can be
    accessed in the globals() namespace.
    """
    # Check existence of the function
    if not hasattr(types, func):
        raise doctest.SkipTest(
            "types.%s not defined -- Python implementation problem." % func)
    # Check type of the function
    if (not isinstance(getattr(types, func),
                       type(types.FunctionType))):
        raise doctest.SkipTest(
            "types.%s not a function type -- Python implementation problem."
            % func)
    # Check it has the expected namespace
    if not globals().has_key(func):
        raise doctest.SkipTest(
            "types.%s not found in globals() namespace -- Python "
            "implementation problem." % func)
    # Check it is in the expected namespace
    if (
