import types
# Test types.FunctionType is callable
f = types.FunctionType(lambda: None, globals())
f()

# Test types.BuiltinFunctionType is callable
f = types.BuiltinFunctionType(len)
f([1, 2, 3])

# Test types.BuiltinMethodType is callable
f = types.BuiltinMethodType(list.append, [])
f(1)

# Test types.MethodType is callable
f = types.MethodType(list.append, [])
f(1)

# Test types.BuiltinMethodDescriptorType is callable
f = list.append
f([], 1)

# Test types.MethodDescriptorType is callable
f = list.__dict__['append']
f([], 1)

# Test types.MemberDescriptorType is not callable
f = list.__dict__['__iter__']
try:
  f()
except TypeError:
  pass

# Test types.GetSetDescriptorType is not callable
f = list.__dict__['__len__']
try:
 
