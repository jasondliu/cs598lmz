import types
types.MethodType(lambda self: self.x, None, A)

# Test that we can't create a method with a non-function
try:
    types.MethodType(1, None, A)
except TypeError:
    pass
else:
    raise Exception("Didn't raise TypeError")

# Test that we can't create a method with a non-class
try:
    types.MethodType(lambda self: self.x, None, 1)
except TypeError:
    pass
else:
    raise Exception("Didn't raise TypeError")

# Test that we can't create a method with a non-instance
try:
    types.MethodType(lambda self: self.x, 1, A)
except TypeError:
    pass
else:
    raise Exception("Didn't raise TypeError")

# Test that we can't create a method with a non-instance
try:
    types.MethodType(lambda self: self.x, 1, A)
except TypeError:
    pass
else:
    raise Exception("Didn't raise TypeError")
