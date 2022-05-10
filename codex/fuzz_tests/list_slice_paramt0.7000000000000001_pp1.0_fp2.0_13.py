import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst

class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=[]
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst

class Ref(object):
    def __init__(self,name):
        self.name=name
    def __call__(self,r):
        print "Callable called with",r
        if r is None:
            print "Die"
            del lst[0]
lst=[str()]
a=Ref("a")
b=Ref("b")
c=Ref("c")
a(b)
a(c)
a(None)
print lst

class Ref(object):
    def __init__(self,name,callback):
        self.name=name
        self.callback=callback
    def __call__(self):
        print "Callable
