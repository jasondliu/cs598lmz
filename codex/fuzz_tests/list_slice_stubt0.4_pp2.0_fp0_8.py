import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(lst[0])
keepali0e.append(callback)
wr=weakref.ref(a,callback)
del a
del keepali0e
gc.collect()
print lst
print lst[0]
print wr
print wr()
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is None
print wr() is
