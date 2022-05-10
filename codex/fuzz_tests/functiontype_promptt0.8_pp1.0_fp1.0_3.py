import types
# Test types.FunctionType()
f = types.FunctionType(code,globals(),'add')

# # Test types.BuiltinFunctionType()
# def f(*args):
#     return args[0] + args[1]
# print(types.BuiltinFunctionType(f))

print(f)
print(f(1,2))

# Test types.MethodType()
g = types.MethodType(f,1)
print(g)

# Test types.SimpleNamespace()
n = types.SimpleNamespace(val = 1)
print(n.val)

# Test types.ModuleType()
# m = types.ModuleType('Houdini','')
# print(m)

# Test types.Name

# Test types.GetSetDescriptorType()
class MyClass(object):
    def __get__(self,instance,cls):
        print("MyClass get")
        return self
    def __set__(self, instance, value):
        print("MyClass set")
        return self
    def __delete__(self, instance):
       
