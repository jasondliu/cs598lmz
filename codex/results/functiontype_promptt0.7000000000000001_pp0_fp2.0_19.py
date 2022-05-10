import types
# Test types.FunctionType
assert type(lambda x: x) is types.FunctionType
# Test types.ClassType
assert type(Exception) is types.ClassType
# Test types.MethodType
class Test(object):
    def __init__(self):
        self.a = 5

    def test(self, x):
        return x * self.a

test = Test()
assert type(test.test) is types.MethodType
# Test types.TypeType
assert type(Test) is types.TypeType
assert type(object) is types.TypeType
# Test types.UnboundMethodType
assert type(Test.__init__) is types.UnboundMethodType
# Test types.TracebackType
try:
    raise Exception()
except Exception, e:
    assert type(e.__traceback__) is types.TracebackType
# Test types.BuiltinFunctionType
assert type(print) is types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(int) is types.BuiltinFunctionType
assert type(str) is types.BuiltinFunctionType
