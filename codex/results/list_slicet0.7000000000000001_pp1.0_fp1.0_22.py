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
print lst
#print keepali0e
import gc
gc.collect()
print lst
del lst
print keepali0e
#print a.c
print "a.c"==str(a.c)
#print a.c
print "a.c"==str(a.c)
