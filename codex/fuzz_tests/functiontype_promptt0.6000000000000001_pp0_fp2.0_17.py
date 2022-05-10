import types
# Test types.FunctionType
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance((x for x in range(10)), types.GeneratorType))
# Test types.MethodType
print(isinstance('abc', types.MethodType))
# Test types.UnboundMethodType
print(isinstance(str.join, types.UnboundMethodType))
# Test types.BuiltinMethodType
print(isinstance(str.upper, types.BuiltinMethodType))
# Test types.BuiltinMethodType
print(isinstance(str.split, types.BuiltinMethodType))
# Test types.ModuleType
print(isinstance(types, types.ModuleType))
# Test types.TracebackType
try:
    10 / 0
except:
    print(isinstance(sys.exc_info()[2], types.TracebackType))
# Test types.FrameType
def bar():
    print(isinstance(sys._getframe(), types.FrameType))
bar()
# Test types.CodeType
print(
