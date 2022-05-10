import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e[0]()
keepali0e.append(weakref.ref(a,callback))
keepali0e[1]()
keepali0e.append(weakref.ref(a,callback))
keepali0e[2]()
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(len(keepali0e)):
    keepali0e[i]()
print lst
