import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
del a
#print lst
#print keepali0e[0]()

#print keepali0e[0]() is keepali0e[0]()

#print keepali0e[0]().c is keepali0e[0]()

#print keepali0e[0]().c is keepali0e[0]()
#print keepali0e[0]().c is keepali0e[0]()
#print keepali0e[0]().c is keepali0e[0]()

#print keepali0e[0]().c is keepali0e[0]()
#print keepali0e[0]().c is keepali0e[0]()

#print keepali0e[0]().c is keepali0e[0]()
#print keepali0e[0]().c is keepali0e[0]()

#print keepali0e[0]().c is keepali0e[0]()
#print keepali0e[0]().c is keepali0e[0
