import types
# Test types.FunctionType
try:
    types.FunctionType(lambda x: x)
except Exception as e:
    print('SKIP')
    raise SystemExit

f = lambda x: x

print(type(f))
print(type(f) == types.FunctionType)
print(isinstance(f, types.FunctionType))

# Test types.LambdaType
try:
    types.LambdaType(lambda x: x)
except Exception as e:
    print('SKIP')
    raise SystemExit

f = lambda x: x

print(type(f))
print(type(f) == types.LambdaType)
print(isinstance(f, types.LambdaType))

# Test types.GeneratorType
def gen():
    yield

g = gen()

print(type(g))
print(type(g) == types.GeneratorType)
print(isinstance(g, types.GeneratorType))

# Test types.CoroutineType
async def coro():
    await

co = coro()

print(type
