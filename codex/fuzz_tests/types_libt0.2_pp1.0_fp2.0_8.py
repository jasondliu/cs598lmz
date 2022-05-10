import types
types.MethodType(lambda self: self.x, None, A)

# this is a function
def f(self):
    return self.x

# this is a method
m = types.MethodType(f, None, A)

# this is a method
m = A.f

# this is a method
m = A().f

# this is a function
m = A.f.__func__

# this is a function
m = A().f.__func__

# this is a function
m = A.f.__get__(None, A)

# this is a function
m = A().f.__get__(None, A)

# this is a function
m = A.f.__get__(A(), A)

# this is a function
m = A().f.__get__(A(), A)

# this is a function
m = A.f.__get__(A(), object)

# this is a function
m = A().f.__get__(A(), object)

# this is a function
m
