import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
for i in range(100000):
 a1=A()
 keepali0e.append(a1)
 lst.append(a1)
 del a1
 a.c.c=a.c 
 lst.append(a)
callback(lst[0])
