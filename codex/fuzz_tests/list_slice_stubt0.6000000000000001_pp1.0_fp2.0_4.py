import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(callback)
keepalive.append(lst)
print "before weakref"
wr=weakref.ref(a,callback)
print "after weakref"
a=None
keepalive.remove(lst)
keepalive.remove(callback)
keepalive.remove(a)
print "begining of the script"
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(callback)
keepalive.append(lst)
print "before weakref"
wr=weakref.ref(a,callback)
print "after weakref"
keepalive.remove(a)
del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(callback)
keepalive.append(lst)
print "before weakref"
wr=weakref.ref
