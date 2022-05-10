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
print(type(func.__globals__) == types.FrameType)

# Test types.TracebackType
try:
    func()
except:
    import sys
    print(type(sys.exc_info()[2]) == types.TracebackType)

# Test types.ModuleType
print(type(types) == types.ModuleType)

# Test types.MethodType
class A:
    def func(self):
        pass

print(type(A.func) == types.MethodType)

# Test types.UnboundMethodType
class A:
   
