import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
lst.append(a)
lst.append(b)
lst.append(a)
lst.append(b)
for o in lst:
    o.c=o
    keepalive.append(o)
    weakref.ref(o, callback)
    del o
del lst
print gc.collect()
assert len(keepalive)==4


class A(object):pass
a=A()
b=A()
lst=[]
def callback(x):
    lst.append(1)
    b.x = 1
lst.append(a)
lst.append(b)
weakref.ref(a, callback)
del a
del b
print gc.collect()
print lst
