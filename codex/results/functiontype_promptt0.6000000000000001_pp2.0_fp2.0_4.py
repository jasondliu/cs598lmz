import types
# Test types.FunctionType
def func1(a):
    print a
    
class class1(object):
    def func2(self, b):
        print b
        
def myfunc(a,b):
    return a+b

print type(func1)
print type(class1)
print type(class1().func2)
print type(myfunc)

print isinstance(myfunc, types.FunctionType)
print isinstance(func1, types.FunctionType)
print isinstance(class1().func2, types.FunctionType)
print isinstance(myfunc, types.MethodType)
print isinstance(func1, types.MethodType)
print isinstance(class1().func2, types.MethodType)

print dir(class1().func2)

# Test types.MethodType
print type(class1().func2)
print isinstance(class1().func2, types.MethodType)

# Test types.BuiltinFunctionType
print type(type)
print isinstance(type, types.BuiltinFunctionType)

# Test types.TypeType
print type(
