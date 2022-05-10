import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print(lst)
del a
print(lst)
lst.append(str())
print(lst)
weakref.finalize(lst[0],callback,lst)
del lst[0]
print(lst)
