import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.LambdaType

l = lambda: None

assert isinstance(l, types.LambdaType)

# Test types.GeneratorType

def g():
    yield

assert isinstance(g(), types.GeneratorType)

# Test types.BuiltinFunctionType

assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType

assert isinstance([].append, types.BuiltinMethodType)

# Test types.MethodType

class C(object):
    def m(self):
        pass

assert isinstance(C.m, types.MethodType)

# Test types.UnboundMethodType

assert isinstance(C.m, types.UnboundMethodType)

# Test types.ModuleType

assert isinstance(types, types.ModuleType)

# Test types.TracebackType

def f():
    try:
        raise Exception
    except:
        return sys.
