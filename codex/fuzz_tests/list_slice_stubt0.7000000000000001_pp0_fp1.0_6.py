import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a,A
gc.collect()
for i in xrange(2):
    lst.append(str())
    keepalive.append(weakref.ref(lst,callback=callback))
    lst=[str()]
del lst,keepalive
gc.collect()
