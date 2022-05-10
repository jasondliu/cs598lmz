import types
# Test types.FunctionType, types.BuiltinFunctionType and types.WrapperDescriptorType
def f():
    pass
def g():
    pass
class C:
    def f(self):
        pass
    def __init__(self, x):
        pass
x = g
assert type(C.__init__) == types.FunctionType
assert type(f) == types.FunctionType or type(f) == types.BuiltinFunctionType
assert type(type) == types.BuiltinFunctionType
asser
