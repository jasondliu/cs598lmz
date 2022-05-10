import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.s=weakref.ref(a,callback)
b=A()
b.c=b
b.s=weakref.ref(b,callback)
lst.append(a)
lst.append(b)
keepali0e.append(a)
keepali0e.append(b)
del b
del a
print len(lst)
