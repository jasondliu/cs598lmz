import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

lst=None
while keepali0e:
    print keepali0e.pop()()


#print weakref.getweakrefcount(a)

print weakref.getweakrefs(a)

#print weakref.getweakrefs(a)
#callback
#print sys.getrefcount(a)
#print sys.getrefcount(lst)

#print weakref.getweakrefcount(a)
#print a.c
#del a.c
#print a.c
#print weakref.getweakrefs(a)
#print weakref.getweakrefcount(a)
#del a
#print weakref.getweakrefs(lst)
#print weakref.getweakrefs(a)

#print(weakref.getweakrefs(lst))
