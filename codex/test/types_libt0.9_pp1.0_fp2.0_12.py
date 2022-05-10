import types
types.MethodType(lambda obj, name: getattr(obj, name), instance).__name__
