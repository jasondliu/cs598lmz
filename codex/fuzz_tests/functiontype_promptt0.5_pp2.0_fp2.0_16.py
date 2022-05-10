import types
# Test types.FunctionType

def f():
    pass

assert type(f) == types.FunctionType
assert type(f()) == types.NoneType
assert type(abs) == types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType
assert type(int) == types.BuiltinFunctionType
assert type(int) == types.BuiltinFunctionType
assert type(lambda: None) == types.LambdaType
assert type(x for x in range(10)) == types.GeneratorType

class C:
    def f(self):
        pass

assert type(C.f) == types.MethodType
assert type(C().f) == types.MethodType

# Test types.ModuleType

assert type(types) == types.ModuleType

# Test types.TracebackType

def g():
    try:
        1/0
    except:
        import sys
        return sys.exc_info()[2]

assert type(g()) == types.TracebackType

# Test types.FrameType

def h():
    import sys
   
