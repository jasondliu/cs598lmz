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
del lst
print len(keepali0e)
keepalive.append(weakref.ref(keepali0e))
del keepali0e
while keepalive:keepalive.append(keepalive[:])
del keepalive
print "done"
