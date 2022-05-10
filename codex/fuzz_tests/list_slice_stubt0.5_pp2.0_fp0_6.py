import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
a.a=a.b
keepalive.append(a)
lst.append(weakref.ref(a,callback))
a=None
lst=[]
print 'ok'
