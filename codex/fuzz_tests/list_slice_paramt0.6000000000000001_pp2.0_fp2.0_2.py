import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(keepali0e)
print lst
del a
del keepali0e
print len(keepali0e)
print lst
for x in lst:
	print "x=",x

#@-node:zorcanda!.20050401135513:@thin weakref_test.py
#@-leo
