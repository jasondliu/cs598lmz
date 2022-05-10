import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
# Test types.GeneratorType
def f():
    yield 1

assert isinstance(f(), types.GeneratorType)

def f():
    yield from [1, 2]

assert isinstance(f(), types.GeneratorType)
# Test types.MethodType
class C:
    def m(self):
        pass

assert isinstance(C.m, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(sum, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([1, 2, 3].append, types.BuiltinMethodType)
# Test types.MethodDescriptorType
assert isinstance([1, 2, 3].__add__, types.MethodDescriptorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.Traceback
