import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepali0e.append(a)
a=A()
a.b=a
keepali0e.append(a)
a=A()
a.b=a
a.c=a
keepali0e.append(a)
lst.append(a)
lst.append(keepali0e[0])
lst.append(keepali0e[1])
lst.append(keepali0e[2])
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
lst.append(lst)
