import types
# Test types.FunctionType
def myFunc (x):
    return x**2

print type(myFunc)

# Test types.LambdaType
myLambda = lambda x:x**2
print type(myLambda)

myLambda2 = lambda x,y:x*y
print type(myLambda2)

# Test types.BuiltinFunctionType
print type(len)

# Test types.BuiltinMethodType
print type(list.insert)
