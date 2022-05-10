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
lst[0]=a
weakref.ref(b,callback)
del b
del lst
del keepalive
gc.collect()
print 'ok'

#ok
