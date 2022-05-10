import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
#keepali0e.append(weakref('hello',callback))
print keepali0e
print a
del a
for i in range(500000000):print ".",
lst=[str(),str()]
del lst
for i in range(500000000):print ".",
lst=str()
del lst
for i in range(500000000):print ".",
#print lst
