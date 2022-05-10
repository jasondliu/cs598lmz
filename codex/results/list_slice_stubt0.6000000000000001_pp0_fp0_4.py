import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.d=a
a.a=a
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
del a
del lst
print len(keepali0e)

#output:
#0
#why not 1?
