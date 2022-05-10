import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
r=weakref.ref(a.c,callback)
del a
for i in range(int(1e6)):
    l=lst[:]
    l.append(l)
    l.append(lst)
