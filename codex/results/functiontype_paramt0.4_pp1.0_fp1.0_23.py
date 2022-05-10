from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'module' object is not iterable
# list(types.FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'module' object is not iterable
# list(types.BuiltinFunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'module' object is not iterable
# list(types.BuiltinMethodType(lambda x: x, globals(), 'lambda'))

# TypeError: 'module' object is not iterable
# list(types.MethodType(lambda x: x, globals(), 'lambda'))

# TypeError: 'module' object is not iterable
# list(types.ModuleType('lambda'))

# TypeError: 'module' object is not iterable
# list(types.TracebackType(None))

# TypeError: 'module' object is not iterable
# list(types.FrameType(None, None, None, None, None))

# TypeError: 'module' object is not iter
