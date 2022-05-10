import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=weakref.ReferenceType(a,callback)
print b.c
keepalive.append(a)
del a
lst.append(str())
assert len(lst)==1
keepalive.append(b)
del b
print lst
assert len(lst)==0
lst=[str()]
d=[]
a=A()
a.c=a
b=weakref.ReferenceType(a,callback)
d.append(a)
print b.c
del a
del d
lst.append(str())
assert len(lst)==1
d=[]
d.append(b)
del b
print lst
assert len(lst)==0
lst=[str()]
a=A()
a.c=(a,a)
b=weakref.ReferenceType(a,callback)
d=[a,]
print b.c
del d
lst.append(str())
assert len(lst)==1
d=[b,]
print lst
del d
print lst
assert len(
