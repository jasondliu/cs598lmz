import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
a.b=a
lst.append(a)
del a
keepalive.append(lst)
del lst
print("%d objects in total"%len(gc.get_objects()))
