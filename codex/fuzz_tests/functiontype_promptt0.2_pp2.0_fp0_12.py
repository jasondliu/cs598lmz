import types
# Test types.FunctionType
def f():
    pass

def g():
    pass

assert type(f) == types.FunctionType
assert type(g) == types.FunctionType
assert type(f) == type(g)

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) != types.FunctionType

# Test types.MethodType
class C:
    def m(self):
        pass

assert type(C.m) == types.MethodType
assert type(C().m) == types.MethodType
assert type(C.m) != type(C().m)

# Test types.UnboundMethodType
assert type(C.m) == types.UnboundMethodType
assert type(C.m) != types.MethodType

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType
assert type(lambda: None) != types.FunctionType

# Test types.GeneratorType
assert type((x for x in range(10))) == types.GeneratorType

# Test types
