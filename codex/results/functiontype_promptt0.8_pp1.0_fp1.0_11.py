import types
# Test types.FunctionType
TestError(type(lambda x: x) != types.FunctionType,
          "type(lambda x: x) != types.FunctionType")

TestError(type(abs) != types.BuiltinFunctionType,
          "type(abs) != types.BuiltinFunctionType")

TestError(type(int) != types.BuiltinFunctionType,
          "type(int) != types.BuiltinFunctionType")

# Test types.LambdaType
TestError(type(lambda x: x) != types.LambdaType,
          "type(lambda x: x) != types.LambdaType")

# Test types.GeneratorType
def gen(): yield 1
TestError(type(gen()) != types.GeneratorType,
          "type(gen()) != types.GeneratorType")

# Test types.TracebackType
import sys, traceback
tb = sys.last_traceback
TestError(type(tb) != types.TracebackType,
          "type(sys.last_traceback) != types.TracebackType")

# Test
