import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

def f():return 42
class C(object):
    __slots__=('g',)
    def __init__(self):
        self.g=f
print type(vars(C()))

def f1(f):
    def f2(self):
        return f(self)
    return f2

def f3(f):
    def f4(self):
        return f(self)
    return f4

def f5(f):
    def f6(self):
        return f(self)
    return f6

class Test(object):
    @f1
    @f3
    @f5
    def foo(self):
        return 42

class A(object):
    def f(self):pass
class B(A):pass
def f(arg):
    return arg
print f(B())

class A(object):
    def f(self):pass
class B(A):
    def g(self):pass

def f(arg):
    return arg
print f
