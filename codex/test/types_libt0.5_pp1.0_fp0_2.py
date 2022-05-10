import types
types.MethodType(f, None, Spam)
Spam.meth(1)

# You can also add new methods to a class after it is defined.
# To do this, you assign the method to the class name.

def f(self, x, y):
    return min(x, x+y)

class C:
    f = f
    def g(self):
        return 'hello world'
    h = g

c = C()
c.f(1, 2)
c.g()
c.h()

# If a class does not define a __call__() method, then it cannot be called.

class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:', pargs, kargs)

c = Callee()
c(1, 2, 3)
c(1, 2, 3, x=4, y=5)

# When you call a function, the function name is resolved using the local and global scopes.
# When you call a method, the method name is resolved using
