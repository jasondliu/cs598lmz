import types
# Test types.FunctionType()

def test(num):
  print('i am a test function')
  return num

print(type(test))
print(type(test(10)))

print(type(lambda : None))
print(type(lambda : None()))

print(type(int))

# Explicit is better than implicit
# There is a inbuilt function called type() to get the type of the variable

a = lambda : None
print(type(a))
print(type(a()))

# The argument of isinstance must be types defined in the standard
# built-in module or else a type object defined in this or another
# module. Otherwise raises a TypeError exception.

print(isinstance(a, type(lambda : None)))
print(type(lambda : None) == type(a))

print(isinstance(a, types.FunctionType))
print(isinstance(test, types.FunctionType))
print(isinstance(int, types.FunctionType))
print(isinstance(test, types.BuiltinFunctionType))

# If a class object is passed for either argument, the
