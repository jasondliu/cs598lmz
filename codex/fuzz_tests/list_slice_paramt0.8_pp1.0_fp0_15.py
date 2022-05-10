import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback)) #mark a as kept alive
del a
keepal0ve.append(weakref.ref(a))
del a
keepali0e.append(weakref.ref(a,callback))
keepal0ve.append(weakref.ref(a))
del a
keepali0e.append(weakref.ref(a,callback))
keepal0ve.append(weakref.ref(a))
del a
keepali0e.append(weakref.ref(a,callback))
keepal0ve.append(weakref.ref(a))
del a
keepali0e.append(weakref.ref(a,callback))
keepal0ve.append(weakref.ref(a))
"""
