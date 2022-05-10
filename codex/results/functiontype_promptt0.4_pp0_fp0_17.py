import types
# Test types.FunctionType
def f():
    pass
if type(f) != types.FunctionType:
    raise TestFailed, 'type(f) is not FunctionType'
# Test types.LambdaType
g = lambda x=1: x
if type(g) != types.LambdaType:
    raise TestFailed, 'type(g) is not LambdaType'
# Test types.GeneratorType
def h():
    yield 1
if type(h()) != types.GeneratorType:
    raise TestFailed, 'type(h()) is not GeneratorType'
# Test types.BuiltinFunctionType
if type(len) != types.BuiltinFunctionType:
    raise TestFailed, 'type(len) is not BuiltinFunctionType'
# Test types.BuiltinMethodType
if type([].append) != types.BuiltinMethodType:
    raise TestFailed, 'type([].append) is not BuiltinMethodType'
# Test types.UnboundMethodType
class C:
    def meth(self): pass
if type(C.meth) != types.UnboundMethodType
