import types
types.MethodType(lambda self: None, None, None)

# Test that we can create a method with a non-string name.
def f(self):
    pass

class C:
    pass

C.__dict__[1] = types.MethodType(f, None, C)

# Test that we can create a method with a non-string name.
def f(self):
    pass

class C:
    pass

C.__dict__[1] = types.MethodType(f, None, C)

# Test that we can create a method with a non-string name.
def f(self):
    pass

class C:
    pass

C.__dict__[1] = types.MethodType(f, None, C)

# Test that we can create a method with a non-string name.
def f(self):
    pass

class C:
    pass

C.__dict__[1] = types.MethodType(f, None, C)

# Test that we can create a method with a non-string name.
