import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
# Test types.MethodType
class A:
    def f(self): pass
assert type(A.f) is types.FunctionType
assert type(A().f) is types.MethodType
# Test types.BuiltinMethodType
assert type(A.__init__) is types.BuiltinMethodType
assert type(A().__init__) is types.BuiltinMethodType
# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
# Test types.GeneratorType
assert type((x for x in range(10))) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
# Test types.FrameType
assert type(sys._getframe()) is types.FrameType
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
assert type(tb) is types.Tr
