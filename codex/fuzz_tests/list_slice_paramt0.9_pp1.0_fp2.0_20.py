import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
print [x() for x in keepali0e]
b=a.c
del a
del b
print [x() for x in keepali0e]
print lst
