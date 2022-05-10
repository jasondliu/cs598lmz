import types
types.MethodType(lambda self: self.foo, obj)

# test that we can call a method
def f(self):
    return self.foo
obj.bar = types.MethodType(f, obj)
obj.bar()

# test that we can call a method on a class
def f(self):
    return self.foo
C.bar = types.MethodType(f, C)
C.bar(obj)

# test that we can call a method on a class
def f(self):
    return self.foo
C.bar = types.MethodType(f, C)
C.bar(obj)

# test that we can call a method on a class
def f(self):
    return self.foo
C.bar = types.MethodType(f, C)
C.bar(obj)

# test that we can call a method on a class
def f(self):
    return self.foo
C.bar = types.MethodType(f, C)
C.bar(obj)

# test that we can call a method on a class
