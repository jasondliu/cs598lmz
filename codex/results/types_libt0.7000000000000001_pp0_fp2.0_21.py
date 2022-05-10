import types
types.MethodType(mod_method,x)

z = types.MethodType(mod_method,x)
print(z)

x.modify()
print(x.s)

print(x)

print(mod_method)
print(mod_method.__self__)

print(mod_method.__func__)
print(mod_method.__func__.__self__)
print(mod_method.__func__.__self__.__class__)

print(z)

# print(z.__self__)
# print(z.__self__.__class__)
# print(z.__self__.__class__.__name__)

print(z.__func__)
print(z.__func__.__self__)
print(z.__func__.__self__.__class__)
print(z.__func__.__self__.__class__.__name__)

print(x)
