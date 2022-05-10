import types
types.MethodType(foo, D)

# Verify that we can't add a method to an instance
# Note that we cannot use the same code as above, because we don't have
# a class with a __set__ method that allows us to add a method to an
# instance

def f(self, x): pass
try:
    f.__set__(None, D)
except TypeError:
    pass
else:
    print("Shouldn't be able to add a method to an instance")

# Verify that we can't add a method to a class
def f(self, x): pass
try:
    f.__set__(D)
except TypeError:
    pass
else:
    print("Shouldn't be able to add a method to a class")

# Verify that we can't add a method to an instance of a built-in type
def f(self, x): pass
try:
    f.__set__(None, C())
except TypeError:
    pass
else:
    print("Shouldn't be able to add a method to an instance of a built-in type
