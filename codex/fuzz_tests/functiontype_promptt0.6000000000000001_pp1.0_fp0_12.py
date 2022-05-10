import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(int) == types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self): pass
assert type(C().m) == types.MethodType

# Test types.UnboundMethodType
assert type(C.m) == types.UnboundMethodType

# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType

# Test types.GeneratorType
assert type((x for x in range(1))) == types.GeneratorType

# Test types.CodeType
def f(): pass
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    frame = sys._getframe()
   
