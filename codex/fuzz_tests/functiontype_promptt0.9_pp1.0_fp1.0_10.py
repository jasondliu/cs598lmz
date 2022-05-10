import types
# Test types.FunctionType for functions defined by f(x)=x**2
f = lambda x: x**2

# On some platforms, such as Windows, types.FunctionType is not recognized, so use type(f) instead.
if types.FunctionType == type(f):
    print("OK")
else:
    print("types.FunctionType is not used.")
    

# Define a class FooType, create an instance of this class, 
# and test whether the instance belongs to class FooType
class FooType(object):
    pass

fooInstance = FooType()
if isinstance(fooInstance, FooType):
    print("fooInstance belongs to FooType")
else:
    print("An instance of FooType is not recognized.")

# You can also make check on types of data, such as:
myInt = 1
myFloat = 1.0
myString = '2'

# The following line uses type() instead of isinstance()
if type(myInt) == int and type(myFloat) == float and type(myString) == str:
    print("OK")
else:
    print("
