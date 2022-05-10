import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(lst)
lst.append(weakref.ref(lst,callback))
del a
del lst
del keepalive
gc.collect()
print "ok"
