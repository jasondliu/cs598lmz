import types
types.MethodType(lambda self: self.x, None, None)

# Test that we can create a bound method from a function and an object
def f(self):
    return self.x

class C:
    x = 1

c = C()
m = types.MethodType(f, c)
assert m() == 1

# Test that we can create a bound method from a function and a class
class C:
    x = 1

c = C()
m = types.MethodType(f, C)
assert m(c) == 1

# Test that we can create a bound method from a function and a type
class C:
    x = 1

c = C()
m = types.MethodType(f, type(c))
assert m(c) == 1

# Test that we can create a bound method from a function and a type
class C:
    x = 1

c = C()
m = types.MethodType(f, type(c))
assert m(c) == 1

# Test that we can create a bound method from a function and a type

