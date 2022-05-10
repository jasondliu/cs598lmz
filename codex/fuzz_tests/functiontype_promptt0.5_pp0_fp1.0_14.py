import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    print('SKIP')
    raise SystemExit

def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
try:
    types.LambdaType
except AttributeError:
    print('SKIP')
    raise SystemExit

g = lambda : 0
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
try:
    types.GeneratorType
except AttributeError:
    print('SKIP')
    raise SystemExit

def h(): yield
assert isinstance(h(), types.GeneratorType)

# Test types.CoroutineType
try:
    types.CoroutineType
except AttributeError:
    print('SKIP')
    raise SystemExit

async def i(): pass
assert isinstance(i(), types.CoroutineType)
