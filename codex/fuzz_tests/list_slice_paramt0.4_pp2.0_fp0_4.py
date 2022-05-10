import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst
print keepali0e
print keepali0e[0]()
print keepali0e[1]()

#print keepali0e[0]().c
#print keepali0e[1]().c
print '-'*30
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst
print keepali0e
print keepali0e[2]()
print keepali0e[3]()

#print keepali0e[2]().c
#print keepali0e[3]().c
