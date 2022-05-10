import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a

def bad():
    "Sets __class__ at runtime"
    
    class D(object):
        def __init__(self,x):
            self.x=x
        def method(self):
            pass
    class C(D):pass
    d1=D(1)
    d2=D(2)
    del D
    d2.__class__=C
    def run():
        del d1.x
        del d1
        try:
            d2.method()
        except:
            return lst[0]() is not []
    return run
del lst
y=bad()
keepali0e.append(y)
lst=[0]
y()
del lst

def bad():
    "Holds onto a nested class after it has gone away"
    class B(object):
        class C(object):
            pass
    b=B()
    c=b.C
    del c,b
    def f():
        while 1:
            try:
                del
