import types
# Test types.FunctionType
try:
    types.FunctionType(lambda x: x, globals())
except TypeError:
    print("SKIP")
    raise SystemExit

# Test types.GeneratorType
def gen():
    yield 1
try:
    types.GeneratorType(gen())
except TypeError:
    print("SKIP")
    raise SystemExit
