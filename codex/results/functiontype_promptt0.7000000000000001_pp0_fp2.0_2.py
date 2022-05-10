import types
# Test types.FunctionType
def function(): print("hi")
assert type(function) == types.FunctionType

# Test types.MethodType
class A(object):
    def method(self): pass
a = A()
assert type(a.method) == types.MethodType

# Test types.LambdaType
lam = lambda: None
assert type(lam) == types.LambdaType

# Test types.GeneratorType
gen = (i for i in range(10))
assert type(gen) == types.GeneratorType

# Test types.CoroutineType
async def coro(): pass
assert type(coro) == types.CoroutineType

# Test types.CodeType
assert type((lambda: None).__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except Exception as exc:
    assert type(exc.__traceback__) == types.TracebackType

# Test types.FrameType
def frame_func(): return frame_func.__code__.co_firstlineno
assert type(frame_func.
