import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.c=lst
keepali0e.append(callback)
keepali0e.append(A)
del keepali0e
print(1)
print(lst)
