import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
del a
gc.collect(0)
if len(lst)==2:
	print "pass"
else:
	print "fail"
