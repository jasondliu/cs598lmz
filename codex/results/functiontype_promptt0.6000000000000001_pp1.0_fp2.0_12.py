import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.MethodType
class A:
    def m(self): pass
assert type(A.m) == types.MethodType

# Test types.UnboundMethodType
assert type(A.m) == types.UnboundMethodType
assert type(A.m) == types.MethodType

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType
assert type(x for x in range(2)) == types.GeneratorType

import array
# Test types.GetSetDescriptorType
assert type(array.array.typecode) == types.GetSetDescriptorType

# Test types.MemberDescriptorType
assert type(array.array.typecode) == types.MemberDescriptorType

# Test types.WrapperDescriptorType
assert type(array.array.typecode) == types.Wrapper
