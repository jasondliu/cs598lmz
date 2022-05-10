import types
# Test types.FunctionType
def test_function_type():
    assert type(test_function_type) == types.FunctionType

print(type(test_function_type))

# Test types.LambdaType
print(type(lambda: None))

# Test types.GeneratorType
print(type(x for x in range(10)))

# Test types.ModuleType
print(type(types))

# Test types.BuiltinFunctionType
print(type(len))

# Test types.BuiltinMethodType
print(type([].append))

# Test types.MethodType
class C:
    def meth(self):
        pass

print(type(C.meth))
print(type(C().meth))

# Test types.UnboundMethodType
print(type(C.meth))

# Test types.TracebackType
try:
    raise Exception
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(type(exc_traceback))

# Test types.FrameType
def f():

