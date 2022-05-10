import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
print(len(lst))
print(lst)
lst[0]=weakref.ref(a,callback)
print(len(lst))
print(lst)
