import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType
# Test types.MethodType
class A:
    def m(self): pass
assert type(A().m) == types.MethodType
# Test types.UnboundMethodType
assert type(A.m) == types.UnboundMethodType
# Test types.ClassType
class B: pass
assert type(B) == types.ClassType
# Test types.InstanceType
assert type(B()) == types.InstanceType
# Test types.LambdaType
assert type(lambda: None) == types.LambdaType
# Test types.GeneratorType
assert type((x for x in range(10))) == types.GeneratorType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) == types.TracebackType
# Test types.FrameType

