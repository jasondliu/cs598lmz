import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
b=A()
b.c=a
lst.append(b)
wr=weakref.ref(b,callback)
del b
if len(lst)!=1:
    raise RuntimeError("Test failed")
del wr
if len(lst)!=0:
   raise RuntimeError("Test failed")
del keepalive
