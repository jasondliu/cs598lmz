import types
# Test types.FunctionType works

def foo():
    pass

def bar():
    print('bar')

def baz(x):
    return x*10

foo_type = types.FunctionType(foo.__code__, globals())
bar_type = types.FunctionType(bar.__code__, globals())
baz_type = types.FunctionType(baz.__code__, globals())

print(foo_type())
print(bar_type())
print(baz_type(2))

# Test types.LambdaType works
foo_lambda = types.LambdaType(baz.__code__, globals(), 'baz', (None,), None)
foo_lambda(2)

# This lambda already returns a value, so pass a default of None
bar_lambda = types.LambdaType(bar.__code__, globals(), 'bar', (types.NoneType,), types.NoneType)
bar_lambda()
