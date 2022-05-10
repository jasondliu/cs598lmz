import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(a)
del a
gc.collect()
print len(lst)
print len(keepalive)
del lst
gc.collect()
print len(keepalive)

#weakref.ref(a,callback)
#print keepalive[0]
#a=None
#print keepalive[0]
#del keepalive
#gc.collect()
#print keepalive
#del a
#gc.collect()
#print keepalive
#a=None
#print keepalive
#del keepalive
#gc.collect()
#print keepalive
#a=None
#print keepalive
#del keepalive
#gc.collect()
#print keepalive
#a=None
#print keepalive
#del keepalive
#gc.collect()
#print keepalive
