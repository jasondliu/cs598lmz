import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive.append(a)
del a
gc.collect()
for i in range(1000):
    x=lst[0]
    x=weakref.ref(x,callback)
    keepalive.append(x)
    lst.append(str())
    del x
    if i%100==0:
        print(i)
        gc.collect()
del lst
gc.collect()
</code>

