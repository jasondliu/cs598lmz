import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst.append(a)
assert lst[1] is a
lst.append(a.c)
assert lst[2] is a.c
