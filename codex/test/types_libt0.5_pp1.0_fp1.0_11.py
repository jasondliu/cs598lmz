import types
types.FunctionType.__call__ = types.MethodType.__call__
types.FunctionType.__get__ = types.MethodType.__get__
types.FunctionType.__set__ = types.MethodType.__set__
types.FunctionType.__delete__ = types.MethodType.__delete__

# ------------------------------------------------------------------------------

