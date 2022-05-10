import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst[0]=a
keepalive=lst[0]
d=weakref.WeakKeyDictionary(a,callback)
del lst[0]
print keepalive.b
print keepalive.c
del keepali0e
del d
del keepalive
print a.b
print a.c
for x in [x for x in ()]:
    print x
for x in (x for x in ()):
    print x
