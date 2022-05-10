import types
# Test types.FunctionType

print type(len)
print type(lambda x: x)
print type(len) == types.BuiltinFunctionType
print type(lambda x: x) == types.LambdaType
print type(xrange) == types.BuiltinFunctionType
print type(xrange) == types.FunctionType
# Test types.LambdaType

def f(): pass
class C:
    def g(self): pass

print type(f)
print type(C.f)
print type(C().g)

print type(f) == types.FunctionType
print type(C.f) == types.MethodType
print type(C().g) == types.MethodType
# Test types.MethodType

print type(C.f)
print type(C().g)

print type(C.f) == types.MethodType
print type(C().g) == types.MethodType
# Test types.BuiltinMethodType

print type(list.append)
print type(dict.has_key)

print type(list.append) == types.BuiltinMethodType

