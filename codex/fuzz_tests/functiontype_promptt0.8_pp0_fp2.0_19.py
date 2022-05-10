import types
# Test types.FunctionType and types.LambdaType

f = lambda x: x*x
type(f)
type(lambda x: x*x)
