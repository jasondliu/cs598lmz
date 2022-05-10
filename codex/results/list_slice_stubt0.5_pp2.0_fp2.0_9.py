import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
b=A()
b.c=b
keepalive.append(b)
a.b=weakref.ref(b,callback)
b.a=weakref.ref(a,callback)
del a,b
del keepalive[:]
del lst[:]
print "ok"
</code>

