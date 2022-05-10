import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a
for i in xrange(1000):
    lst.append(weakref.ref(lst,callback))
lst.pop().__call__()
