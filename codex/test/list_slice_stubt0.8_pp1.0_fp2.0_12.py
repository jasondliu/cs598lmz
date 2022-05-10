import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
lst.append(a)
lst.append(a.c)
lst.append(a.b)
lst.append(a.b.c)
lst.append(a.b.c.b)
lst.append(a.b)
lst.append(a.c)
lst.append(a)
lst.append(lst)
lst.append(lst[::])
cbk=lst[::]
cbk.append(callback)
lst.append(cbk)
