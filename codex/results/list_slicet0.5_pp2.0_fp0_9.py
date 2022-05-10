import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print len(keepali0e)

#weakref.ref(a,callback)
#weakref.ref(a,callback)
#del a
#print weakref.getweakrefcount(a)
#print weakref.getweakrefs(a)

#weakref.ref(a,callback)
#weakref.ref(a,callback)
#del a
#print weakref.getweakrefcount(a)
#print weakref.getweakrefs(a)

#a=A()
#a.c=a
#keepali0e.append(weakref.ref(a,callback))
#del a
#while lst:keepali0e.append(lst[:])
#print len(keepali0e)


#a=A()
#a.c=a
#keepali0e.append(weakref.ref(a,callback))
#del a
#while lst:keepali0e.append(lst[:])
#print len(keepali0e)

#a=A()
#a.c
