import types
# Test types.FunctionType
def func():
  pass
def test_FunctionType():
  assert isinstance(func, types.FunctionType)
  assert not isinstance(1, types.FunctionType)
  assert not isinstance(True, types.FunctionType)
  assert not isinstance('s', types.FunctionType)
  assert not isinstance(None, types.FunctionType)

# Test types.LambdaType
test_lambda = lambda: None
def test_LambdaType():
  assert isinstance(test_lambda, types.LambdaType)
  assert not isinstance(1, types.LambdaType)
  assert not isinstance(True, types.LambdaType)
  assert not isinstance('s', types.LambdaType)
  assert not isinstance(None, types.LambdaType)

# Test types.GeneratorType
def generator():
  for i in range(10):
    yield i
def test_GeneratorType():
  assert isinstance(generator(), types.GeneratorType)
  assert not isinstance(1, types.GeneratorType)
