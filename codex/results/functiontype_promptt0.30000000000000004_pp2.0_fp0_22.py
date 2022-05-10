import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.LambdaType

g = lambda: None

assert isinstance(g, types.LambdaType)

# Test types.GeneratorType

def h():
    yield None

assert isinstance(h(), types.GeneratorType)

# Test types.MethodType

class A:
    def __init__(self):
        self.x = 1
    def f(self):
        pass

a = A()
assert isinstance(a.f, types.MethodType)

# Test types.BuiltinFunctionType

assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType

assert isinstance(list.append, types.BuiltinMethodType)

# Test types.ModuleType

assert isinstance(types, types.ModuleType)

# Test types.TracebackType

try:
    raise Exception
except Exception:
    tb = sys.exc_info()[2]
   
