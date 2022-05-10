import types
# Test types.FunctionType and types.GeneratorType
if not hasattr(types, 'FunctionType'):
    print('SKIP')
    raise SystemExit

def test(x):
    yield x

print(type(test), type(print), type(test) == type(print))
print(type(test) == types.GeneratorType)
print(type(lambda : 0))
print(type(lambda : 0) == types.FunctionType)
