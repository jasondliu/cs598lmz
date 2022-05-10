import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
#del a
c=a.c
a.c=None
#del a
a.x=5
#del a
a.x=a
weakref.ref(a,callback)
gc.collect()
print(lst)
