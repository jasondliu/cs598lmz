import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
b=A()
b.b=a
c=A()
c.a=b
keepalive=[a,b,c]
del b
del c
lst[0]=a
callback_obj=weakref.ref(a,callback)
del a
for _ in range(100):collect()

a1=A()
a1.c=a1
a1.d=lst
b1=A()
b1.b=a1
c1=A()
c1.a=b1
keepalive=[a1,b1,c1]
del b1
del c1
lst[0]=a1
callback_obj=weakref.ref(a1,callback)
del a1
for _ in range(100):collect()

collect()
print("Finalizing")
testerror("callback not called in time")
print("OK")
