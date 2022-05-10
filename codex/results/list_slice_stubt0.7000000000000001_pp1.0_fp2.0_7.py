import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print lst
print len(lst)
print lst[0]
print lst[0].c
print type(lst[0])
print type(lst[0].c)



import weakref
class A(object):pass
def callback(x):print x
a=A()
a.c=a
print a.c
r=weakref.ref(a,callback)
print r
print r()
print r().c
del a
print r()
print r().c
print r().c.c
print r().c.c.c
