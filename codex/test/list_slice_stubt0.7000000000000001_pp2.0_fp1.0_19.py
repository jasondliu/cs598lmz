import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive=[a,a.c,a.d,a.c.d,a.c.d.c]
keepalive.append(keepalive)
w=weakref.ref(str,callback)
lst[0]=w
print()
print("前",lst)
del a
a=None
print("后",lst)
del w

print("后",lst)

a=A()
a.b=a
a.c=a
a.d=a
print(a.b.c.d.b)
print(a.b.b.b.b.b)
print(a.b.b.b.b.b.b.b.b.b.b.b.b.b.b.b)
