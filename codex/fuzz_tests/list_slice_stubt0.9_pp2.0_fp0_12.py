import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a
import gc
while keepalive:
	gc.collect()
	for o in gc.get_objects():
		if not isinstance(o,weakref.ReferenceType):
			lst.append(o)
			keepali0e.append(o)
			del lst[:]
			break
print 'ok'
