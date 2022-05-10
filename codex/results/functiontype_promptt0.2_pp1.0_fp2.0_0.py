import types
# Test types.FunctionType
def f():
    pass

print(type(f) is types.FunctionType)

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def f(self):
        pass

print(type(A.f) is types.MethodType)

# Test types.UnboundMethodType
print(type(A.f) is types.UnboundMethodType)

# Test types.LambdaType
print(type(lambda: None) is types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1

print(type(g()) is types.GeneratorType)

# Test types.CodeType
print(type(f.__code__) is types.CodeType)

# Test types.FrameType
def h():
    return h.__code__.__code__.co_filename

print(type(h()) is types.FrameType)

# Test types.TracebackType
import sys
try:
   
