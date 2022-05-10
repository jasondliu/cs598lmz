import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
#print weakref.getweakrefcount(a),a.c
a=A()
a.c=a
lst.append(a)
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print weakref.getweakrefcount(a),a.c
#print lst
