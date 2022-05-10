import types
# Test types.FunctionType, types.LambdaType, types.ClassType, types.TypeType, types.InstanceType

# Test function
def f(x,y):
  return x+y

print types.FunctionType(f.func_code,f.func_globals,f.func_name,f.func_defaults,f.func_closure) == f

# Test lambda
g = lambda x: x**2
print types.LambdaType(g.func_code,g.func_globals,g.func_name,g.func_defaults,g.func_closure) == g

# Test class
class X(object):
  pass

print types.ClassType(X.__name__,X.__bases__,X.__dict__) == X

# Test type
print types.TypeType == type

# Test instance
x = X()
print types.InstanceType(x.__class__) == x
