import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
del keepali0e
del a
import gc;gc.collect()

def a():
    x=1
    def b():
        x+=1
    b()
    return x

class C(object):
    pass
print(C.__dict__)
C.x=1
print(C.__dict__)
d=C()
print(d.__dict__)
d.x=2
print(d.__dict__)
print(d.__class__.__dict__)

class C(object):
    def __init__(self):
        self.x=1
    def method(self):
        print(self.x)

def a(x):
    def b(y):
        return x+y
    print(b(2))
a(1)

def a(x):
    def b(y):
        return x+y
    return b
