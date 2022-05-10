import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType, "FunctionType test failed"

# Test types.BuiltinFunctionType
assert type(id) == types.BuiltinFunctionType, "BuiltinFunctionType test failed"

# Test types.MethodType
class C:
    def f(self):
        pass
assert type(C.f) == types.MethodType, "MethodType test failed"

# Test types.UnboundMethodType
assert type(C.f.im_func) == types.UnboundMethodType, "UnboundMethodType test failed"

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType, "LambdaType test failed"

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) == types.GeneratorType, "GeneratorType test failed"

# Test types.CodeType
assert type(g.func_code) == types.CodeType, "CodeType test failed"

# Test types.TracebackType
try:
    raise Exception
