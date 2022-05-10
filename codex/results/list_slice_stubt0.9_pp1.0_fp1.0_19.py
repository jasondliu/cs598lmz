import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=str(a)
keepalive1=str(a)
keepalive2=weakref.ref(a,callback)
del a
print len(lst)
for i in range(10):gc.collect()
print len(lst)
