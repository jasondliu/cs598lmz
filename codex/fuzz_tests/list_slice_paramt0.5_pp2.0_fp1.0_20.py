import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
print "lst:",lst
print "keepali0e:",keepali0e
print "lst[0]:",lst[0]
print "keepali0e[0]():",keepali0e[0]()
print "lst[1]:",lst[1]
print "lst[2]():",lst[2]()
print "lst:",lst
print "keepali0e:",keepali0e
print "lst[0]:",lst[0]
print "keepali0e[0]():",keepali0e[0]()
print "lst[1]:",lst[1]
print "lst[2]():",lst[2]()
