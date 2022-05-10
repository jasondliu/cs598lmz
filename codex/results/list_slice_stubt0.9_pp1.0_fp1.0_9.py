import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(a)
lst.append(a)
keepalive.append(a)
print len(lst)

gc.collect()
print len(lst)
# print lst
print "after"
print len(keepalive)
lst.append(A())
del lst[0]
print lst[0]
