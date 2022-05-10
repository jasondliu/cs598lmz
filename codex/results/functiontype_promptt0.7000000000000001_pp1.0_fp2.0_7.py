import types
# Test types.FunctionType

def f(x):
    return x

assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType

assert type(id) is types.BuiltinFunctionType

# Test types.MethodType

class C:
    def foo(self):
        pass

assert type(C.foo) is types.MethodType

# Test types.BuiltinMethodType

class D:
    def foo(self):
        pass

assert type(D().foo) is types.BuiltinMethodType

# Test types.ModuleType

assert type(types) is types.ModuleType

# Test types.TracebackType

try:
    1/0
except Exception as e:
    assert type(e.__traceback__) is types.TracebackType

# Test types.FrameType

def g():
    import inspect
    return inspect.currentframe()

assert type(g()) is types.FrameType

# Test types.GetSetDescriptorType

class E:
    def getx(self):
        return self
