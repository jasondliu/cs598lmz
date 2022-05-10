import types
# Test types.FunctionType
def f(): pass
print type(f) is types.FunctionType
print type(lambda x: x) is types.FunctionType
print type((lambda x: x).func_code) is types.CodeType
print type(f.func_code) is types.CodeType

# Test types.LambdaType
print type(lambda x: x) is types.LambdaType
# Bug: see #1430118
#print type((lambda x: (lambda y: x + y))(1)) is types.LambdaType
print type((lambda x: x).func_code) is types.CodeType
print type(f.func_code) is types.CodeType
print type(type) is types.TypeType
print type(1.23) is types.FloatType
print type(0) is types.IntType
print type(0L) is types.LongType
print type(X()) is types.InstanceType
print type(type(1.23)) is types.TypeType
print type(types.InstanceType) is types.TypeType

# Test types.ClassType
# Warning
