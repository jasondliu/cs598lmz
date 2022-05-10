import types
types.MethodType(lambda self: None, None, cls)

# Test that we can create a class with a method that has a closure.
def f(x):
    def g(y):
        return x + y
    return g

class C:
    pass

C.m = f(1)
C().m(2)

# Test that we can create a class with a method that has a closure
# over a class variable.
class D:
    x = 1
    def f(self):
        def g(y):
            return self.x + y
        return g

D.m = D().f()
D().m(2)

# Test that we can create a class with a method that has a closure
# over a class variable that is defined after the method.
class E:
    def f(self):
        def g(y):
            return self.x + y
        return g
    x = 1

E.m = E().f()
E().m(2)

# Test that we can create a class with a method that has a closure

