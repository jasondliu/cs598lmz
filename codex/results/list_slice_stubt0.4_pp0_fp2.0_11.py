import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
print "a:",a
print "w:",w
print "lst:",lst
del a
print "a:",a
print "w:",w
print "lst:",lst
del lst[0]
print "lst:",lst
print "w:",w
