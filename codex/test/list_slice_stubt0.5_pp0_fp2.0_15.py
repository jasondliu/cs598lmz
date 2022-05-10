import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
for i in range(10):
    a.b.c=a
    a.b=a
    del a.b
    a.b=a
    a.b.c=a
