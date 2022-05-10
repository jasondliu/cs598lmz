import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))

del a
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
del lst

from weakref import WeakKeyDictionary
class A(object):pass
B=WeakKeyDictionary()
a=A()
a.b=a
B[a]=5
print B
from weakref import WeakValueDictionary
a=A()
a.b=a
B=WeakValueDictionary()
B[5]=a
B
def Get_Score():
    info=[('Chrome',90),('Firefox',70),('IE',60)]
    return info
def B(L):
    def A(name):
        for i in L:
            if i[0]==name:
                return i[1]
    return A
def A():
    L=Get_Score()
    return B(L)
score=A()
score('Chrome')
del L
class Foo(object):
    def __init__(self,a
