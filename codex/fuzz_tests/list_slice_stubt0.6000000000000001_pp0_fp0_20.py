import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
lst.append(a)
keepalive.append(a)
del a
print(len(lst))
print(lst)
print(keepalive)
print(lst[0])
