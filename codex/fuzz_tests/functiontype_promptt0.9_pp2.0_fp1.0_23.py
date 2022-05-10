import types
# Test types.FunctionType
assert type(lambda: None) == types.FunctionType

# Test types.LambdaType
def lambda_func1(): return lambda: None
# No longer works
# assert type(lambda_func1()) == types.LambdaType

# Test types.MethodType
class MethodTypeTest(object):
    def method(self, x):
        '''method docstring'''
        pass
assert type(MethodTypeTest()) is not types.MethodType
assert type(MethodTypeTest().method) == types.MethodType


# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type(MethodTypeTest().method) == types.MethodType

# Test types.GeneratorType
def generator(): yield 1; yield 2; yield 3
assert type(generator()) == types.GeneratorType

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType
assert type(types) == types.ModuleType

# Test types.GetSetDescriptorType
class A(object):

