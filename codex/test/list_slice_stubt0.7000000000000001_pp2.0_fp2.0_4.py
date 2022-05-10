import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.c.c=a.c
w=weakref.ref(a,callback)
del a
keepali0e.append(w)
del w
lst.append(str())
del lst
print('ok')
