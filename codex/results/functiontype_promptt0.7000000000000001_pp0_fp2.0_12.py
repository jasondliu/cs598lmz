import types
# Test types.FunctionType

# This is not a function...
def f():
    pass

# ... so this should fail
try:
    types.FunctionType(f)
except TypeError:
    print("TypeError")

# But this works
def g():
    pass

types.FunctionType(g)

# And the same for methods
class A:
    def m(self):
        pass

a = A()

# This fails
try:
    types.FunctionType(a.m)
except TypeError:
    print("TypeError")

# This works
types.FunctionType(A.m)

# And the same for static methods
class B:
    @staticmethod
    def m():
        pass

# This fails
try:
    types.FunctionType(B.m)
except TypeError:
    print("TypeError")

# This works
def h():
    pass

types.FunctionType(h)
