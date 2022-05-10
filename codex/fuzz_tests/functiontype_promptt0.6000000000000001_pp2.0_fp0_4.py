import types
# Test types.FunctionType()
def f(): pass
assert isinstance(f, types.FunctionType)
assert f() is None

# Test types.MethodType()
class C(object):
  def f(self):
    return self

assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)
assert C().f() is C()

# Test types.BuiltinFunctionType()
assert isinstance(abs, types.BuiltinFunctionType)
assert isinstance(C.f.__get__(None), types.BuiltinFunctionType)

# Test types.BuiltinMethodType()
assert isinstance(C().f, types.BuiltinMethodType)

# Test types.UnboundMethodType()
assert isinstance(C.f, types.UnboundMethodType)

# Test types.LambdaType()
l = lambda x:x
assert isinstance(l, types.LambdaType)
assert l(1) == 1

# Test types.GeneratorType()
def f():
  yield 1
  yield 2

g =
