import types
# Test types.FunctionType( )
def testfunction(a,b):
    return a+b

if type(testfunction)==types.FunctionType:
    print "The type of testfunction is FunctionType"
else:
    print "The type of testfunction is not FunctionType"

print type(testfunction)
print types.FunctionType

print type(testfunction)==types.FunctionType
print type(testfunction) is types.FunctionType
print type(testfunction)

# Test types.BuiltinFunctionType( )
if type(abs)==types.BuiltinFunctionType:
    print "The type of abs is BuiltinFunctionType"
else:
    print "The type of abs is not BuiltinFunctionType"

print type(abs)
print types.BuiltinFunctionType
print type(abs)==types.BuiltinFunctionType
print type(abs) is types.BuiltinFunctionType
print type(abs)

# Test types.LambdaType( )
print type(lambda x:x)
print types.LambdaType
print type(lambda x:x)==types.Lamb
