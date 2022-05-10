import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print(lst)
lst.append(weakref.ref(a.c,callback))
print(lst)
keepalive.remove(a)
del a
print(lst)
print(lst[0]())
print(lst)
