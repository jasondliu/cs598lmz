import types
# Test types.FunctionType
def func(arg):
    return arg

assert type(func) == types.FunctionType
# Test types.LambdaType
lambda_func = lambda arg: arg

assert type(lambda_func) == types.LambdaType
# Test types.GeneratorType
def generator():
    yield 1

assert type(generator()) == types.GeneratorType
# Test types.CodeType
def code_func():
    return func.func_code

assert isinstance(code_func(), types.CodeType)
# Test types.TracebackType
try:
    raise Exception()
except Exception as exc:
    assert isinstance(exc.__traceback__, types.TracebackType)
# Test types.FrameType
assert type(func.func_code.co_frame) == types.FrameType
# Test types.BuiltinFunctionType
assert type(func) == types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type(func.func_code) == types.BuiltinMethodType
# Test types.MethodType
class Foo(object):
    def
