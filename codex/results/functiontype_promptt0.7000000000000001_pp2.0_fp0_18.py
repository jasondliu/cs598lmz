import types
# Test types.FunctionType
if isinstance(lambda: None, types.FunctionType):
    raise Exception("Function type is not working!")
else:
    print("Function type is working!")


# Test types.LambdaType
# TODO: Currently, there is no way to detect lambda type
# BTW: Python's lambda type is different from C's lambda. C's lambda is just a function,
# while Python's lambda is a function with limited usage.

# Test types.GeneratorType
# TODO: Currently, there is no way to detect this type


# Test types.TracebackType
# TODO: Currently, there is no way to detect this type


# Test types.FrameType
# TODO: Currently, there is no way to detect this type


# Test types.CodeType
def test_code_type():
    pass


if isinstance(test_code_type.__code__, types.CodeType):
    print("Code type is working!")
else:
    raise Exception("Code type is not working!")


# Test types.BuiltinFunctionType
if isinstance(test_
