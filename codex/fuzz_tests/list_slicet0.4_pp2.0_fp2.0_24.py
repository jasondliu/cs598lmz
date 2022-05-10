import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(lst)

# 可以看到，虽然a的引用计数为0，但是由于a.c引用了a，所以a的引用计数不为0，所以a不会被回收，而a.c也不会被回收，所以a.c.c也不会被回收，所以a.c.c.c也不会被回收，以此类推，所以a.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.
