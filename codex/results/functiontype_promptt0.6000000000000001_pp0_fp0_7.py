import types
# Test types.FunctionType by creating a trivial function
def f1(a,b):
    return a+b

print(f1)
print(type(f1))
print(type(f1) is types.FunctionType)

# Test types.LambdaType by creating a trivial lambda
f2 = lambda a,b: a+b

print(f2)
print(type(f2))
print(type(f2) is types.LambdaType)

#Test types.GeneratorType by creating a trivial generator
def f3(x):
    yield x*x

f4 = f3(4)
print(f4)
print(type(f4))
print(type(f4) is types.GeneratorType)

#Test types.GeneratorType by creating a trivial generator
def f5(x):
    yield x*x

f6 = f5(4)
print(f6)
print(type(f6))
print(type(f6) is types.GeneratorType)

#Test types.GeneratorType by creating a trivial generator
def
