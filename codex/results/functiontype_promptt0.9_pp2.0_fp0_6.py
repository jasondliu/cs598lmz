import types
# Test types.FunctionType
def test_function_type(env):
  mod = env.import_module(test_src)
  f = mod.foo
  assert is_instance(f, types.FunctionType)
  # NB: bar is a C++-level lambda, not a Python-level one
  g = mod.bar
  assert is_instance(g, types.FunctionType)

# Test types.LambdaType
def test_lambda_type(env):
  mod = env.import_module(test_src)
  f = mod.f
  assert is_instance(f, types.LambdaType)

# Test types.MethodType
def test_method_type(env):
  mod = env.import_module(test_src)
  C = mod.C
  f = C().f
  assert is_instance(f, types.MethodType)
  f2 = mod.C.f
  assert is_instance(f2, types.MethodType)

# Test types.BuiltinFunctionType
def test_builtin_function_type(env):
  import built
