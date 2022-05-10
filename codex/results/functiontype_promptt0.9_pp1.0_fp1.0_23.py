import types
# Test types.FunctionType and types.BuiltinFunctionType
if types.FunctionType is not None:
    class F(object):
        def f(self): return 42
    def g(): return "hello"
    def g(): return "world"
    print(types.FunctionType(F.f.__func__.__code__, {}, None, None, None))
    print(types.BuiltinFunctionType(g.__code__, {}, None, None, None))
