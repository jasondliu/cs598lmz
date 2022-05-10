import types
# Test types.FunctionType and types.LambdaType
# types.LambdaType is a subtype of types.FunctionType

print('Calling a function...')

def foo():
	pass

print(type(foo) == types.FunctionType)
print(type(foo) == types.LambdaType)

print('Calling a lambda...')

bar = lambda:None
print(type(bar) == types.FunctionType)
print(type(bar) == types.LambdaType)

print('Calling a lambda, but assigned to a function...')

def bar():
	pass

print(type(bar) == types.FunctionType)
print(type(bar) == types.LambdaType)

print('Creating a function object...')

foo = types.FunctionType(compile('pass', '', 'eval'), globals(), 'foo')
print(type(foo) == types.FunctionType)
print(type(foo) == types.LambdaType)

print('Creating a lambda object...')

bar = types.LambdaType(compile('pass',
