import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.v=str()
a.w=str()
lst.append(a)
print(lst)
weakref.ref(a,callback)
keepalive.append(a.w)
del a.w
del a.v
del a.c
lst[0]="hello"
print(lst)
print(weakref.getweakrefcount(a))
print(weakref.getweakrefs(a))
print(keepalive)
