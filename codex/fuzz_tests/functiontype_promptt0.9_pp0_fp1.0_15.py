import types
# Test types.FunctionType
print(types.FunctionType)
# Test types.CodeType
print(types.CodeType)
# Test types.BuiltinFunctionType
print(types.BuiltinFunctionType)

# Test types.GeneratorType
# x = (print() for _ in range(10))
# print(x)
# print(type(x))
# print(isinstance(x, types.GeneratorType))

# Test types.LambdaType

# Test types.ClassType
class Name:
    def __init__(self):
        pass

class_A = Name()
print(type(class_A))
print(isinstance(class_A, Name))
print(isinstance(class_A, types.InstanceType))
print(isinstance(class_A, types.TypeType))
