import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print len(lst)
del a,lst
print len(keepalive)
#结果是2
class A(object):pass
def callback(x):print "callback"
keepalive=[]
lst=[]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print len(lst)
del a
print len(keepalive)

#结果是1
