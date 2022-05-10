import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
import weakref
class A(object):pass
def callback(x):print(x)
class B(object):
    def __init__(self,a):
        self.a=a
def callback(x):
    print(x)
a=A()
b=B(a)
a.b=b
a.b=None
a.b=b
del b
ko=[]
ko.append(weakref.ref(a,callback))
del a
ko
a=A()
ko=[]
ko.append(weakref.ref(a,callback))
del a
ko
a=A()
ko=[]
ko.append(weakref.ref(a,callback))
ko[0]().b
ko[0]().b
ko[0]().b
ko[0]()
ko[0]()
ko[0]()
ko
ko[0].__call__()
ko[0].__call__()
ko[0].__call__()
ko[0]()
ko[0
