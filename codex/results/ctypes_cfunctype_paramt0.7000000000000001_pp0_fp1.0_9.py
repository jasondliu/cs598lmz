import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_int)
def myfunc(i):
    return i%2
newfunc = FUNTYPE(myfunc)
if newfunc(4):
    print "even"
else:
    print "odd"

#class-based function type
class MyFunc(object):
    def __init__(self, val):
        self.val=val
    def __call__(self, i):
        return i%self.val
newfunc = FUNTYPE(MyFunc(3))
print [newfunc(i) for i in range(10)]

#Assigning functions to variables
def f(x):
    return x*2
g = f
print g(2)
print g is f

#Passing functions as arguments
def f(x, y, func):
    print func(x) + func(y)
f(3, 4, g)

#Returning functions
def f():
    def g():
        return 'hello'
    return g

x = f()
print x()

#Inner functions
