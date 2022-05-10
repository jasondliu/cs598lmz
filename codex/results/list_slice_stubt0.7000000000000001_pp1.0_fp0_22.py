import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print weakref.getweakrefcount(a),weakref.getweakrefcount(a.c)
weakref.ref(a,callback)
print weakref.getweakrefcount(a),weakref.getweakrefcount(a.c)
del a
print weakref.getweakrefcount(a),weakref.getweakrefcount(a.c)
del lst
