import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print id(a)
keepalive=weakref.ref(a,callback)
while lst:
    print keepalive,len(gc.get_referents(a))
    print len(lst)
    print len(keepali0e)
    del a
    keepali0e.append(a)
    a=A()
    a.c=a
    print id(a)
    keepaive=weakref.ref(a,callback)
