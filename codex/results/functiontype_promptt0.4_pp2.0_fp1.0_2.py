import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
# Test types.LambdaType
l = lambda: None
assert type(l) is types.LambdaType
# Test types.GeneratorType
g = (i for i in range(10))
assert type(g) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
assert type(l.__code__) is types.CodeType
assert type(g.gi_code) is types.CodeType
# Test types.MethodType
class A:
    def f(self): pass
assert type(A.f) is types.MethodType
assert type(A().f) is types.MethodType
# Test types.BuiltinMethodType
assert type(len) is types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
assert type({}.get) is types.BuiltinMethodType
# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType
assert type(min) is types.Built
