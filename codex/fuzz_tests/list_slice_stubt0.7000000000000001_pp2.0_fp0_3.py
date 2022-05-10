import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
lst.append(a)
del a
del lst[0]
print 'ok'
#keepalive
#lst=[]
#a=A()
#a.c=a
#keepalive.append(a)
#lst.append(str())
#del lst[0]
#del a
#print 'ok'
#keepalive
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
del keepalive[0]
print 'ok'
#lst=[]
#a=A()
#a.c=a
#keepalive.append(a)
#lst.append(str())
#w=weakref.ref(a.c,callback)
#del lst[0]
#del keepalive[0]
#print 'ok'
