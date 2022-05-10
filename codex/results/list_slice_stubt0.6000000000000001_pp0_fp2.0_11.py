import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a,lst]
#del a
print(a)
del a
print(a)
lst[0]=weakref.ref(a,callback)
print(lst)
print(lst[0])
print(lst[0]().c)
print(lst)
del a
print(lst)
#print(lst[0])
