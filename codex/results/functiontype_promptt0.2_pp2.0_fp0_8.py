import types
# Test types.FunctionType
def f(): pass
print type(f) == types.FunctionType

# Test types.LambdaType
g = lambda x: x
print type(g) == types.LambdaType

# Test types.GeneratorType
def h():
    yield 1
    yield 2
print type(h()) == types.GeneratorType

# Test types.CodeType
print type(f.func_code) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    print type(sys.exc_traceback) == types.TracebackType

# Test types.FrameType
def i():
    print type(sys._getframe()) == types.FrameType
i()

# Test types.BuiltinFunctionType
print type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
print type([].append) == types.BuiltinMethodType

# Test types.ModuleType
import types
print type(types) == types.ModuleType

# Test types.UnboundMethodType

