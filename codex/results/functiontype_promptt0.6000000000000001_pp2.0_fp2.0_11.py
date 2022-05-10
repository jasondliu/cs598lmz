import types
# Test types.FunctionType
def func_test():
    print("Function test")

if type(func_test) == types.FunctionType:
    print("Function")

# Test types.BuiltinFunctionType
if type(len) == types.BuiltinFunctionType:
    print("BuiltinFunctionType")

# Test types.LambdaType
if type(lambda x: x) == types.LambdaType:
    print("LambdaType")

# Test types.GeneratorType
def gen():
    yield 1

if type(gen()) == types.GeneratorType:
    print("GeneratorType")

# Test types.CodeType
if type(gen.__code__) == types.CodeType:
    print("CodeType")

# Test types.FrameType
def frame_test():
    print("Frame test")
    return frame_test

if type(frame_test()) == types.FrameType:
    print("FrameType")

# Test types.TracebackType
if type(gen.__code__.__traceback__) == types.TracebackType:
