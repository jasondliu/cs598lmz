import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=a
lst[0]=weakref.ref(lst[0],callback)
print lst
print keepalive
print '\n'
keepalive[0].c=None
print lst
print keepalive
print '\n'
keepalive[0]=None
print lst
print keepalive
print '\n'
del keepalive[0]
print lst
print keepalive
print '\n'
del lst[0]
print lst
print keepalive
print '\n'
del keepalive[0]
print lst
print keepalive
print '\n'
del lst[0]
print lst
print keepalive
print '\n'
del keepalive[0]
print lst
print keepalive
print '\n'
del lst[0]
print lst
print keepalive
print '\n'
del keepalive[0]
print lst
print keepalive
print '
