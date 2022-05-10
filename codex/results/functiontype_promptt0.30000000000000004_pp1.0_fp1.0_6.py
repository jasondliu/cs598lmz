import types
# Test types.FunctionType
def func():
    pass
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.CodeType
def func():
    pass
print(type(func.__code__) == types.CodeType)

# Test types.FrameType
def func():
    pass
print(type(func.__code__.co_frame) == types.FrameType)

# Test types.TracebackType
def func():
    pass
print(type(func.__code__.co_frame.f_trace) == types.TracebackType)

# Test types.ModuleType
print(type(sys) == types.ModuleType)

# Test types.MethodType
class A:
    def func(self):
        pass
print(type(A.func) == types.MethodType)

# Test types.UnboundMethodType
class
