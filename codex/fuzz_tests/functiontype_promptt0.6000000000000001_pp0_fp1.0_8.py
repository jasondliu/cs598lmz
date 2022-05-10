import types
# Test types.FunctionType

def f():
    pass

assert type(f) is types.FunctionType

def g():
    def h():
        pass
    return h

assert type(g()) is types.FunctionType
# Test types.BuiltinFunctionType

assert type(abs) is types.BuiltinFunctionType

# Test types.MethodType

class C:
    def f(self):
        pass

assert type(C.f) is types.MethodType
assert type(C().f) is types.MethodType

def f():
    def g():
        pass
    return g

g = f()
assert type(g) is types.FunctionType

# Test types.LambdaType

assert type(lambda x: x) is types.LambdaType

# Test types.GeneratorType

def f():
    yield 1

assert type(f()) is types.GeneratorType

# Test types.CodeType

def f():
    pass

assert type(f.__code__) is types.CodeType

# Test types.Traceback
