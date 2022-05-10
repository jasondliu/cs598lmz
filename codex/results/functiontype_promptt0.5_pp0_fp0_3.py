import types
# Test types.FunctionType
def t1():
    pass

assert isinstance(t1, types.FunctionType)
# Test types.MethodType
class A:
    def t2(self):
        pass

assert isinstance(A.t2, types.MethodType)
a = A()
assert isinstance(a.t2, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(A.__add__, types.BuiltinMethodType)
assert isinstance(a.__add__, types.BuiltinMethodType)
# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CodeType
assert isinstance(t1.__code__, types.CodeType)
# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.
