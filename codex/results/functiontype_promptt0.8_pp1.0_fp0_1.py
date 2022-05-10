import types
# Test types.FunctionType

# Here's our mock

def m(self, x, y, z):
    print(self, x, y, z)
    return self, x, y, z

c = 1

# Here's our instance bound method

i = types.MethodType(m, c)

i(2, 3, 4)

# Here's our class bound method

def foo():
    pass

m = types.MethodType(m, foo, type(foo))

m(foo, 2, 3, 4)

# Here's a function

f = types.FunctionType(m.__code__, m.__globals__)

f(3, 4, 5, 6)

# Here's a function with a different global dict

g = types.FunctionType(m.__code__, {'c': 9})

g(4, 5, 6, 7)

# Here's a function with its own definitions of __globals__ and __name__

h = types.FunctionType(m.__code__, {'c': 9}, __
