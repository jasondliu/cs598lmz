import types
# Test types.FunctionType
def func(): pass
f = types.FunctionType(func.__code__,globals())
assert f.__name__ == "func"
# Test types.MethodType
class A:
    def method(self):
        return self
a = A()
method = types.MethodType(A.method,a)
assert method().__class__ is A
# Test types.GeneratorType
def gen():
    yield 1
g = gen()
assert type(g) is types.GeneratorType
assert next(g) == 1
# Test types.CoroutineType
async def coro():
    return 1
c = coro()
assert type(c) is types.CoroutineType
assert 1 == await c


# Test types.AsyncGeneratorType
async def agen():
    yield 1
ag = agen()
assert type(ag) is types.AsyncGeneratorType
assert 1 == await ag.asend(None)

# Test types.TracebackType
try:
    raise Exception
except Exception:
    tb = sys.exc_info()[2]
