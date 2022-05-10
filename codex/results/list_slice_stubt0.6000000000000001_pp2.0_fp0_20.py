import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
a.a=a.c
keepalive.append(a)
del a
del keepalive
gc.collect()
if lst:
	print "** failed"
	del lst
	gc.collect()
	if lst:print "** really failed"
else:
	print "** passed"
	del lst
	gc.collect()
	if lst:print "** really failed"
print "** creating circular reference to object"
keepalive=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
a.a=a.c
keepalive.append(a)
del a
del keepalive
gc.collect()
if lst:
	print "** failed"
	del lst
	gc.collect()
	if lst:print "** really failed"
else:
	print "** passed"
	del lst
	gc.collect()
	if lst:print "** really failed"
print "** creating circular reference to type
