import types
# Test types.FunctionType
def get_name(fn):
    """Return the name of a function"""
    if isinstance(fn, types.FunctionType):
        return fn.__name__

def get_names(fn):
    """Return the names of all functions"""
    if isinstance(fn, types.FunctionType):
        return [fn.__name__]
    elif isinstance(fn, types.BuiltinFunctionType):
        return [fn.__name__]
    elif isinstance(fn, types.MethodType):
        return [fn.__name__]
    elif isinstance(fn, types.BuiltinMethodType):
        return [fn.__name__]
    elif isinstance(fn, types.LambdaType):
        return [fn.__name__]
    elif isinstance(fn, types.GeneratorType):
        return [fn.__name__]
    elif isinstance(fn, types.CodeType):
        return [fn.__name__]
    elif isinstance(fn, types.TracebackType):
        return [fn.__
