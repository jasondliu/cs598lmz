import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
print weakref.getweakrefcount(a)
print weakref.getweakrefs(a)
del a
while lst:a=1
print
print weakref.getweakrefcount(a)
print weakref.getweakrefs(a)
print lst
