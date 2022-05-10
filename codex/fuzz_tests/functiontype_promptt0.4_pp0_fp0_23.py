import types
# Test types.FunctionType
def func(): pass
print(type(func) is types.FunctionType)
# Test types.LambdaType
print(type(lambda: None) is types.LambdaType)
# Test types.GeneratorType
def gen():
    yield 1
print(type(gen()) is types.GeneratorType)
# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)
# Test types.BuiltinMethodType
print(type([].append) is types.BuiltinMethodType)
# Test types.MethodType
class A:
    def method(self):
        pass
print(type(A().method) is types.MethodType)
# Test types.UnboundMethodType
print(type(A.method) is types.UnboundMethodType)
# Test types.ModuleType
import sys
print(type(sys) is types.ModuleType)
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    print(type(tb) is types.Tr
