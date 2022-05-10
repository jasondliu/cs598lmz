import types
types.MethodType(lambda self: None, None, None)

# Test that we can create a bound method with a lambda
class C:
    pass

C.m = types.MethodType(lambda self: None, None, C)
C().m()

# Test that we can create a bound method with a function
def f(self):
    pass

C.m = types.MethodType(f, None, C)
C().m()

# Test that we can create a bound method with a method
class D:
    def f(self):
        pass

C.m = types.MethodType(D().f, None, C)
C().m()

# Test that we can create an unbound method with a lambda
C.m = types.MethodType(lambda self: None, None, None)
C.m(C())

# Test that we can create an unbound method with a function
def f(self):
    pass

C.m = types.MethodType(f, None, None)
C.m(C())

# Test that we can create an unbound
