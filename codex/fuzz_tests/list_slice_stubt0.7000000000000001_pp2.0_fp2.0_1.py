import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=str(a)
keepalive=a
for i in range(20):
	a=A()
	a.c=a
	lst[0]=str(a)
	keepalive=a
	keepalive=lst
	sys.getrefcount(lst)
	del lst
	lst=[str()]
	keepalive=lst
	keepalive=a
	keepalive=callback
	keepalive=lst
	del a
	del callback
	del keepalive
	"""
	if i>0:
		keepalive=lst
		keepalive=a
		keepalive=callback
		del a
		del callback
		del keepalive
	"""
	print "iteration",i
