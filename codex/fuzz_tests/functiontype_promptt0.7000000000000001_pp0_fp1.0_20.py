import types
# Test types.FunctionType
f = types.FunctionType(code, globals())
print(f())
print(f.__name__)
print(f.__code__)
print(f.__defaults__)
print(f.__globals__)
print(f.__kwdefaults__)
print(f.__closure__)
print(f.__annotations__)
print(f.__doc__)
print(f.__module__)
print(f.__dict__)

# Test types.MethodType
m = types.MethodType(f, None)
print(m())
print(m.__self__)
print(m.__func__)
print(m.__doc__)

# Test types.BuiltinMethodType
b = types.BuiltinMethodType(None)
print(b.__self__)
print(b.__func__)
print(b.__doc__)

# Test types.MethodDescriptorType
md = types.MethodDescriptorType(None)
print(md.__objclass__)
print(md.__
