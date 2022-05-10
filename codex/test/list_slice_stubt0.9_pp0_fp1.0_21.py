import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=callback
keepali0e.append(a)
del a
del A
del keepali0e
print(lst)
