import types
types.CodeType = types.CodeType
types.MethodType = types.MethodType
types.BuiltinMethodType = types.BuiltinMethodType
types.FunctionType = types.FunctionType
types.BuiltinFunctionType = types.BuiltinFunctionType
types.LambdaType = types.LambdaType
types.GeneratorType = types.GeneratorType
types.TracebackType = types.TracebackType
types.FrameType = types.FrameType


def _is_magic(name):
    return name.startswith('__') and name.endswith('__')


# XXX: The following functions are missing:
# inspect.formatargspec
# inspect.formatannotation


class _EmptyClass:
    pass

def ismodule(object):
    """Return true if the object is a module.

    Module objects provide these attributes:
        __doc__         documentation string
        __file__        filename (missing for built-in modules)
    """
    return isinstance(object, types.ModuleType)

def isclass(object):
    """Return true if the object is a
