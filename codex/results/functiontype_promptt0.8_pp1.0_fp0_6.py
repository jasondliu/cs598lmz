import types
# Test types.FunctionType and types.LambdaType
def passLambda(lambdaFunction):
    return lambdaFunction(3, 4)

def passFunction(function):
    return function(5, 6)

print(passLambda(lambda x, y: x+y))

print(passFunction(lambda x, y: x+y))

print(passLambda(lambda x, y: x*y))

print(passFunction(lambda x, y: x*y))

print(passLambda(None))

print(passFunction(None))



# Test types.TypeType
print(type(type))
print(type(None))
print(type(3))
print(type(3.14))
print(type('hello'))
print(type(type(3)))
print(type(passFunction))
print(type(passLambda))
print(type(passFunction(lambda x,y: x+y)))
print(type(passLambda(lambda x,y: x+y)))



# Test types.GeneratorType
def gen
