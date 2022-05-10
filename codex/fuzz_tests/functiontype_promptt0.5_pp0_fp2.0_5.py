import types
# Test types.FunctionType

def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda:None, types.FunctionType)
assert not isinstance(3, types.FunctionType)

# Test types.LambdaType

assert isinstance(lambda:None, types.LambdaType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(3, types.LambdaType)

# Test types.GeneratorType

def g():
    yield 1
assert isinstance(g(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(3, types.GeneratorType)

# Test types.CodeType

#assert isinstance(f.func_code, types.CodeType)
#assert isinstance(g.func_code, types.CodeType)
#assert isinstance(lambda:None.func_code, types.CodeType)
#assert not isinstance(3, types.CodeType)

# Test types.TracebackType

try:
   
