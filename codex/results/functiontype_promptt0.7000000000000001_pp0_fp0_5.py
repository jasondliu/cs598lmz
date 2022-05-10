import types
# Test types.FunctionType
assert type(lambda x: x) == types.FunctionType
assert type(lambda: None) == types.FunctionType
assert type(lambda x=False: x) == types.FunctionType
# Test types.LambdaType
assert type(eval("(lambda: None)")) == types.LambdaType
assert type(eval("(lambda x: x)")) == types.LambdaType
assert type(eval("(lambda x=False: x)")) == types.LambdaType
# Test types.GeneratorType
assert type((lambda: (yield))()) == types.GeneratorType
assert type((lambda: (yield None))()) == types.GeneratorType
# Test types.CodeType
assert hasattr(types, 'CodeType')
assert type(lambda: None).__code__ == types.CodeType
# Test types.BuiltinFunctionType
assert hasattr(types, 'BuiltinFunctionType')
assert type(map) == types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert hasattr(types, 'BuiltinMethodType')
assert type(map.__init
