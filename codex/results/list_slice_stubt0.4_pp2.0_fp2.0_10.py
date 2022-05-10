import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
wr=weakref.ref(a,callback)
del a
print(lst)
print(wr)
print(wr())
print(lst)
