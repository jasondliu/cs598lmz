import types
# Test types.FunctionType
def foo():
    pass

print(type(foo) is types.FunctionType)
print(type(foo) is types.BuiltinFunctionType)
print(type(foo) is types.BuiltinMethodType)
print(type(foo) is types.MethodType)
print(type(foo) is types.LambdaType)
print(type(foo) is types.UnboundMethodType)
print(type(foo) is types.ModuleType)
print(type(foo) is types.ClassType)
print(type(foo) is types.TypeType)
print(type(foo) is types.TracebackType)
print(type(foo) is types.FrameType)
print(type(foo) is types.CodeType)
print(type(foo) is types.FileType)
print(type(foo) is types.XRangeType)
print(type(foo) is types.SliceType)
print(type(foo) is types.EllipsisType)
print(type(foo) is types.DictProxyType)
print(type(foo) is types.
