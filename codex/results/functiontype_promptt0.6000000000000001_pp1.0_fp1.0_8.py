import types
# Test types.FunctionType
def func(x):
    return x
assert isinstance(func, types.FunctionType)
# Test types.LambdaType
lam = lambda x: x
assert isinstance(lam, types.LambdaType)
# Test types.GeneratorType
gen = (x for x in range(10))
assert isinstance(gen, types.GeneratorType)
# Test types.CodeType
assert isinstance(func.__code__, types.CodeType)
assert isinstance(lam.__code__, types.CodeType)
assert isinstance(gen.gi_code, types.CodeType)
# Test types.TracebackType
try:
    raise Exception
except Exception as e:
    assert isinstance(e.__traceback__, types.TracebackType)
# Test types.FrameType
def new_func():
    return types.FrameType(new_func.__code__, {}, 'tmp.py', 1, False, None)
assert isinstance(new_func(), types.FrameType)
# Test types.GetSetDescriptorType
class A(object):
