import types
# Test types.FunctionType
if type(lambda: None) != types.FunctionType:
    print("Failed")
# Test types.LambdaType
if type(lambda: None) != types.LambdaType:
    print("Failed")
# Test types.GeneratorType
def gen():
    yield 1
if type(gen()) != types.GeneratorType:
    print("Failed")
# Test types.GeneratorType
def gen():
    yield 1
if type(gen()) != types.GeneratorType:
    print("Failed")
# Test types.BuiltinFunctionType
if type(lambda: None) != types.BuiltinFunctionType:
    print("Failed")
# Test types.BuiltinMethodType
if type(lambda: None) != types.BuiltinMethodType:
    print("Failed")
# Test types.ModuleType
if type(types) != types.ModuleType:
    print("Failed")
# Test types.GetSetDescriptorType
class A:
    def __get__(self, key, default):
        pass
    def __set__(self,
