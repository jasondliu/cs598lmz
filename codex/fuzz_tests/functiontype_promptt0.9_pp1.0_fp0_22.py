import types
# Test types.FunctionType()
def test_1_1():
  import types
  assert isinstance(my_abs, types.BuiltinFunctionType)

# Test types.LambdaType()
def test_1_2():
  import types
  x = lambda a, b, c: a + b + c
  assert isinstance(x, types.LambdaType)

# Test types.GeneratorType()
def test_1_3():
  import types
  import sys
  def f():
    yield 1
    yield 2
    yield 3
  g = f()
  #generator generators iterators
  assert isinstance(g, types.GeneratorType)
  #assert isinstance(g, types.GeneratorType)
  #assert isinstance(g, types.GeneratorType)

# Test types.TracebackType()
def test_1_4():
  import types
  try:
    raise Exception('test_1_4')
  except Exception as e:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.
