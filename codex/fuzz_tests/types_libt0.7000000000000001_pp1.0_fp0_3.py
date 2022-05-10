import types
types.MethodType

# a method can be bound to an instance or unbound
# an unbound method is a function that is a member of a class
# a bound method is an instance attribute
# bound methods are invoked on an instance
# unbound methods are invoked on a class
class C1:
    def f1():
        print('f1')

c1 = C1()
c1.f1() # bound method
C1.f1() # unbound method

class C2:
    def f1(self):
        print('f1')

c2 = C2()
c2.f1()
C2.f1(c2)
C2.f1() # TypeError: f1() missing 1 required positional argument: 'self'

# special methods
# attribute access 
class C3:
    def __init__(self):
        self.a = 0
        self.b = 0
    def __getattr__(self, name):
        if name == 'c':
            return self.a + self.b
        else:
            raise AttributeError()
