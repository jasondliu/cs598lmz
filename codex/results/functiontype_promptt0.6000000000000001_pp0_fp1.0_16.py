import types
# Test types.FunctionType
def is_function(f):
    return isinstance(f, types.FunctionType)

# Test types.GeneratorType
def is_generator(g):
    return isinstance(g, types.GeneratorType)

# Test types.GeneratorType
def is_generator(g):
    return isinstance(g, types.GeneratorType)

# Test types.BuiltinMethodType
def is_builtin_method(m):
    return isinstance(m, types.BuiltinMethodType)

# Test types.LambdaType
def is_lambda(l):
    return isinstance(l, types.LambdaType)

# Test types.UnboundMethodType
def is_unbound_method(m):
    return isinstance(m, types.UnboundMethodType)

# Test types.MethodType
def is_method(m):
    return isinstance(m, types.MethodType)

# Test types.TracebackType
def is_traceback(t):
    return isinstance(t, types.TracebackType)


