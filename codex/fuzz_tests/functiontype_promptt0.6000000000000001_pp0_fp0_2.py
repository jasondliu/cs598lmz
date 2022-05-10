import types
# Test types.FunctionType for Python 3.x compatibility
if str(types.FunctionType) == "<class 'function'>":
    def isfunction(obj):
        return isinstance(obj, types.FunctionType)
else:
    def isfunction(obj):
        return hasattr(obj, '__call__')


def get_callable_name(obj):
    """Return a name for the callable object.
    This function tries its best to return a useful name for the input
    object. If the object is a class or a method, the name of the
    class or method will be returned. If the object is a function or
    a functor, the name of the function or functor will be returned.
    Otherwise, for other callable objects, a string representation
    of the callable object will be returned.
    """
    if isinstance(obj, type):
        return obj.__name__
    if hasattr(obj, '__func__'):
        obj = obj.__func__
    if hasattr(obj, '__name__'):
        return obj.__name__
    return str(obj)
