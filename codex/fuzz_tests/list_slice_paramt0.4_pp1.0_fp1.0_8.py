import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

def f():
    for i in range(100):
        a=A()
        a.c=a
        lst.append(a)
        keepali0e.append(weakref.ref(a,callback))
    del a
    del lst
    return keepali0e

def g():
    for i in range(100):
        a=A()
        a.c=a
        lst.append(a)
        keepali0e.append(weakref.ref(a,callback))
    del a
    del lst
    return keepali0e

def h():
    for i in range(100):
        a=A()
        a.c=a
        lst.append(a)
        keepali0e.append(weakref.ref(a,callback))
    del a
    del lst
    return keepali0e

def i():
    for i in range(100):
        a=A()
        a.c=a
        lst.append(a)
       
