import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(lst)
del a
print(lst)

#3
import weakref
class A(object):pass
a=A()
b=A()
c=A()
a.b=b
b.c=c
c.a=a
print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))
print(weakref.getweakrefcount(c))
print(weakref.getweakrefs(a))
print(weakref.getweakrefs(b))
print(weakref.getweakrefs(c))
