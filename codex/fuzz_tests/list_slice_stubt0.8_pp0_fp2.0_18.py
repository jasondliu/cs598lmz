import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del keepalive

#print weakref.getweakrefcount(lst[0])

#print weakref.getweakrefs(lst[0])

#print weakref.ref(lst[0],callback)

#print weakref.proxy(lst[0])#无效

#weakref.finalize(lst,del lst[0])
print lst

#print weakref.getweakrefcount(lst)
#print weakref.getweakrefs(lst)

print weakref.ref(lst,callback)

print weakref.proxy(lst)
print weakref.getweakreflist(lst)

weakref.finalize(lst,del lst[0])
print lst
