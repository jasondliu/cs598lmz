import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print(a)
keepalive=a

del a
print(lst)
del keepalive
print(lst)
