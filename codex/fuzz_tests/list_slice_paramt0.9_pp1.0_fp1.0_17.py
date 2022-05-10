import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print weakref.getweakrefcount(a),weakref.getweakrefcount(str()),lst
del a
print lst
del keepali0e
print lst
