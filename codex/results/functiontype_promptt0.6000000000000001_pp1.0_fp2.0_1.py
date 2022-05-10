import types
# Test types.FunctionType, types.MethodType, types.LambdaType, types.CodeType, types.ClassType

# FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(lambda: 1) is types.FunctionType

# MethodType
assert type(f.__call__) is types.MethodType
assert type(str.upper) is types.MethodType
assert type(str.upper.__call__) is types.MethodType

# LambdaType
assert type(lambda: 1) is types.LambdaType

# CodeType
c = f.__code__
assert type(c) is types.CodeType

# ClassType
assert type(str) is types.ClassType
assert type(int) is types.ClassType

# type(object)
assert type(object) is types.TypeType

# type(str)
assert type(str) is types.TypeType

# type(type)
assert type(type) is types.TypeType

# type(int)
assert type(int) is types.TypeType
