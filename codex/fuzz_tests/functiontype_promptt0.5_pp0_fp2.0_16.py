import types
# Test types.FunctionType
def f():
    pass
print(type(f) is types.FunctionType)
print(type(lambda x: x) is types.LambdaType)
# Test types.MethodType
class C:
    def meth(self):
        pass
print(type(C.meth) is types.MethodType)
# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)
# Test types.BuiltinMethodType
print(type([].append) is types.BuiltinMethodType)
# Test types.ModuleType
import sys
print(type(sys) is types.ModuleType)
# Test types.TracebackType
try:
    raise Exception()
except:
    exc_type, exc_value, exc_tb = sys.exc_info()
print(type(exc_tb) is types.TracebackType)
# Test types.FrameType
def g():
    import sys
    return sys._getframe()
print(type(g()) is types.FrameType)
# Test types.CodeType
print(type(g
