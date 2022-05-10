import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del a
gc.collect()
while keepalive:
	gc.collect()
	time.sleep(0.1)
print 'Done.'
