import types
# Test types.FunctionType

def f():
    pass

assert type(f) == types.FunctionType
# Test types.BuiltinFunctionType

assert type(len) == types.BuiltinFunctionType
# Test types.TypeType

assert type(int) == types.TypeType
assert type(type) == types.TypeType
# Test types.UnboundMethodType

class C(object):
    def f(self):
        pass

assert type(C.f) == types.UnboundMethodType
# Test types.InstanceType

assert type(C()) == types.InstanceType
# Test types.MethodType

assert type(C().f) == types.MethodType
# Test types.GeneratorType

def g():
    yield 1

assert type(g()) == types.GeneratorType
# Test types.CodeType

assert type(f.func_code) == types.CodeType
# Test types.TracebackType

try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) == types.TracebackType
# Test types.Frame
