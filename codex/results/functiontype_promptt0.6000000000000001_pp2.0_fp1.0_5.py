import types
# Test types.FunctionType, types.ClassType, types.BuiltinFunctionType, and types.BuiltinMethodType.

print isinstance(lambda x: x, types.FunctionType)
print isinstance(lambda x: x, types.BuiltinFunctionType)

class X(object):
  def __init__(self):
    pass

print isinstance(X, types.ClassType)
print isinstance(X, types.TypeType)
print isinstance(X, types.BuiltinFunctionType)

print isinstance(X.__init__, types.FunctionType)
print isinstance(X.__init__, types.BuiltinFunctionType)
print isinstance(X.__init__, types.BuiltinMethodType)

class Y(object):
  def __init__(self):
    pass

print isinstance(Y.__init__, types.FunctionType)
print isinstance(Y.__init__, types.BuiltinFunctionType)
print isinstance(Y.__init__, types.BuiltinMethodType)

class Z(object):
  def __init__(self):
   
