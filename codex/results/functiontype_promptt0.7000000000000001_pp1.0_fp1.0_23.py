import types
# Test types.FunctionType and types.MethodType
# Use type comparison (isinstance) to test type
# For methods, need to use __self__ to test the instance

class A():
    def f(self):
        print "A.f()"

class B(A):
    def f(self):
        print "B.f()"

class C(B):
    def f(self):
        print "C.f()"

# test type FunctionType
def foo(a):
    a.f()

# test type MethodType
class m:
    def __init__(self, o):
        self.o = o

    def run(self):
        self.o.f()

# create objects of the classes
a = A()
b = B()
c = C()

# create the methods
af = A.f
bf = B.f
cf = C.f

# create the objects for methods
am = m(a)
bm = m(b)
cm = m(c)

# create the lambda
lam = lambda o: o.f()

