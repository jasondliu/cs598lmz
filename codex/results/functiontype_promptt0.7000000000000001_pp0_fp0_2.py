import types
# Test types.FunctionType
def test_types_function():
    assert isinstance(test_types_function, types.FunctionType)
    print(types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
print(types.LambdaType)

# Test types.GeneratorType
assert isinstance(range(10), types.GeneratorType)
print(types.GeneratorType)

# Test types.CodeType
assert isinstance(test_types_function.__code__, types.CodeType)
print(types.CodeType)

# Test types.TypeType
assert isinstance(int, types.TypeType)
print(types.TypeType)

# Test types.UnboundMethodType
import types
class C:
    def method(self): pass
assert isinstance(C.method, types.UnboundMethodType)
print(types.UnboundMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)
print(types.ModuleType)

# Test types.Trace
