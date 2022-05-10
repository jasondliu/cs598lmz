import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
print len(lst)
del a.c
print len(lst)
print len(lst)
del a.b
print len(lst)
