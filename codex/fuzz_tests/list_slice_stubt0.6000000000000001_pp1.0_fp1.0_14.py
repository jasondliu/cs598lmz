import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
lst.append(a)
lst.append(callback)
keepalive.append(lst)
lst=None
a=None
print "gc.collect()=",gc.collect()
print "len(keepalive)=",len(keepalive)
print "len(keepali0e)=",len(keepali0e)
print "done"
